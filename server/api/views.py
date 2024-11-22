from rest_framework import generics
from .models import Item
from .serializers import ItemSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import authenticate, login, logout
from django.db.models import Q
from .models import Room, Topic, Messages, User
from rest_framework import status
from .serializers import (
    RoomSerializer,
    UserSerializer,
    MessageSerializer,
    TopicSerializer,
)
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.tokens import UntypedToken
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
from rest_framework.permissions import IsAuthenticated
from .permissions import AuthenticateUser, IsOwnerOrRoom, CustomIsAuthenticated


######## authenticate user views  #######
class LoginPageView(APIView):
    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")

        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            refresh = RefreshToken.for_user(user)
            response = Response()
            response.set_cookie(
                key="access_token",
                value=str(refresh.access_token),
                httponly=True,
                samesite="Lax",
            )
            response.set_cookie(
                key="refresh_token", value=str(refresh), httponly=True, samesite="Lax"
            )
            response.data = {
                "access_token": str(refresh.access_token),
                "refresh_token": str(refresh),
            }
            return response
        else:
            return Response(
                {"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED
            )


class LogoutUserView(APIView):
    def post(self, request):
        logout(request)
        response = Response({"message": "Logout successful"}, status=status.HTTP_200_OK)
        response.delete_cookie("access_token")
        response.delete_cookie("refresh_token")
        return response


class RegisterUserView(APIView):
    def post(self, request):
        user = User.objects.filter(
            Q(email=request.data.get("email"))
            | Q(username=request.data.get("username"))
        )
        if user.exists():
            return Response(
                {"error": "Invalid username or email"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            user.username = user.username.lower()
            user.save()
            return Response(
                {"message": "Registration successful"}, status=status.HTTP_201_CREATED
            )
        else:
            errors = [error[0] for error in serializer.errors.values()]
            return Response(
                {"error": " ".join(errors)}, status=status.HTTP_400_BAD_REQUEST
            )


class UserProfileView(APIView):
    def get(self, request, pk):
        try:
            user = User.objects.get(id=pk)
        except User.DoesNotExist:
            return Response(
                {"error": "User not found"}, status=status.HTTP_404_NOT_FOUND
            )

        rooms = user.room_set.all()
        room_messages = user.messages_set.all()
        topics = Topic.objects.all()
        data = {
            "user": UserSerializer(user).data,
            "rooms": RoomSerializer(rooms, many=True).data,
            "room_messages": MessageSerializer(room_messages, many=True).data,
            "topics": TopicSerializer(topics, many=True).data,
        }
        return Response(data, status=status.HTTP_200_OK)


######## authenticate user views  #######
class ShowCurrentUser(APIView):
    def get(self, request):
        token = request.COOKIES.get("access_token")
        if not token:
            return Response(
                {"error": "Unauthorized access, no token"},
                status=status.HTTP_401_UNAUTHORIZED,
            )

        try:
            # Verify the token and get the payload
            payload = UntypedToken(token)
            user_id = payload.get("user_id")
            if not user_id:
                return Response(
                    {"error": "Unauthorized access,invalid token"},
                    status=status.HTTP_401_UNAUTHORIZED,
                )

            # Get the user from the database
            user = User.objects.get(id=user_id)
            return Response(UserSerializer(user).data, status=status.HTTP_200_OK)

        except (InvalidToken, TokenError) as e:
            return Response(
                {"error": "Invalid Token"}, status=status.HTTP_401_UNAUTHORIZED
            )


class UpdateUserView(APIView):
    def patch(self, request):
        try:
            res = ShowCurrentUser().get(request)
            if res.status_code != 200:
                return Response(
                    {"error": "User not found"}, status=status.HTTP_404_NOT_FOUND
                )

            user = User.objects.get(id=res.data["id"])
        except User.DoesNotExist:
            return Response(
                {"error": "User not found"}, status=status.HTTP_404_NOT_FOUND
            )

        serializer = UserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User updated"}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


######## Rooms view  #######
class HomeView(APIView):
    def get(self, request):
        q = request.GET.get("q") if request.GET.get("q") else ""
        rooms = Room.objects.filter(
            Q(topic__name__icontains=q)
            | Q(name__icontains=q)
            | Q(description__icontains=q)
        )
        topics = Topic.objects.all()[0:10]
        room_count = rooms.count()
        room_messages = Messages.objects.filter(room__topic__name__icontains=q)[0:3]
        data = {
            "rooms": RoomSerializer(rooms, many=True).data,
            "topics": TopicSerializer(topics, many=True).data,
            "room_count": room_count,
            "room_messages": MessageSerializer(room_messages, many=True).data,
        }
        return Response(data, status=status.HTTP_200_OK)


class RoomView(APIView):
    def get(self, request, pk):
        room = Room.objects.get(id=pk)
        room_messages = room.messages_set.all().order_by("-created")
        participants = room.participants.all()
        data = {
            "room": RoomSerializer(room).data,
            "room_messages": MessageSerializer(room_messages, many=True).data,
            "participants": UserSerializer(participants, many=True).data,
        }
        return Response(data, status=status.HTTP_200_OK)

    def post(self, request, pk):
        room = Room.objects.get(id=pk)
        message = Messages.objects.create(
            user=request.user, room=room, body=request.data.get("body")
        )
        room.participants.add(request.user)
        return Response({"message": "Message created"}, status=status.HTTP_201_CREATED)


class GetAllRoomsView(APIView):
    def get(self, request):
        rooms = Room.objects.all()
        serializer = RoomSerializer(rooms, many=True)
        return Response(
            {"rooms": serializer.data, "count": rooms.count()},
            status=status.HTTP_200_OK,
        )


class CreateRoomView(APIView):
    def post(self, request):
        topic_name = request.data.get("topic")
        topic, created = Topic.objects.get_or_create(name=topic_name)

        try:
            user = AuthenticateUser().is_authenticated(request)
            user_id = user.get("id")
            host = user_id
        except Exception as e:
            return Response(
                {"error": "Unauthorized access"}, status=status.HTTP_403_FORBIDDEN
            )

        if not host:
            return Response(
                {"error": "Unauthorized access"}, status=status.HTTP_403_FORBIDDEN
            )

        room_data = {
            "host": host,
            "topic": topic.id,
            "name": request.data.get("name"),
            "description": request.data.get("description"),
        }
        serializer = RoomSerializer(data=room_data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "Room created", "data": serializer.data},
                status=status.HTTP_201_CREATED,
            )
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UpdateRoomView(APIView):
    def patch(self, request, pk):
        room = Room.objects.get(id=pk)
        try:
            user = AuthenticateUser().is_authenticated(request)
            user_id = user.get("email")
        except Exception as e:
            return Response(
                {"error": "Unauthorized access"}, status=status.HTTP_403_FORBIDDEN
            )

        if not user:
            return Response(
                {"error": "Unauthorized access"}, status=status.HTTP_403_FORBIDDEN
            )

        if user_id != room.host.email:
            return Response(
                {"error": "You are not allowed here"}, status=status.HTTP_403_FORBIDDEN
            )

        topic_name = request.data.get("topic")
        topic, created = Topic.objects.get_or_create(name=topic_name)
        room_data = {
            "name": request.data.get("name"),
            "topic": topic.id,
            "description": request.data.get("description"),
        }
        serializer = RoomSerializer(room, data=room_data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "Room updated", "dat": serializer.data},
                status=status.HTTP_200_OK,
            )
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DeleteRoomView(APIView):
    permission_classes = [CustomIsAuthenticated, IsOwnerOrRoom]

    def delete(self, request, pk):
        try:
            room = Room.objects.get(id=pk)
        except Room.DoesNotExist:
            return Response(
                {"error": "Room not found"}, status=status.HTTP_404_NOT_FOUND
            )

        user = AuthenticateUser().is_authenticated(request)
        if not user:
            return Response(
                {"error": "Unauthorized access"}, status=status.HTTP_403_FORBIDDEN
            )

        try:
            user_id = user.get("id")
            room_id = room.host.id
        except Exception as e:
            return Response(
                {"error": "Unauthorized access"}, status=status.HTTP_403_FORBIDDEN
            )

        if user_id != room_id:
            return Response(
                {"error": "You are not allowed here"}, status=status.HTTP_403_FORBIDDEN
            )

        room.delete()
        return Response({"message": "Room deleted"}, status=status.HTTP_200_OK)


class SendMessageView(APIView):
    permission_classes = [CustomIsAuthenticated]

    def post(self, request, pk):
        res = ShowCurrentUser().get(request)
        if res.status_code != 200:
            return Response(
                {"error": "User not found"}, status=status.HTTP_404_NOT_FOUND
            )

        user_data = res.data
        user = User.objects.get(id=user_data["id"])
        try:
            room = Room.objects.get(id=pk)
        except Room.DoesNotExist:
            return Response(
                {"error": "Room not found"}, status=status.HTTP_404_NOT_FOUND
            )

        message = Messages.objects.create(
            user=user, room=room, body=request.data.get("body")
        )

        room.participants.add(request.user)
        return Response({"message": "Message created"}, status=status.HTTP_201_CREATED)


class MessageActionsView(APIView):
    permission_classes = [CustomIsAuthenticated]

    # update message

    def patch(self, request, pk):
        try:
            message = Messages.objects.get(id=pk)

        except Messages.DoesNotExist:
            return Response(
                {"error": "Message not found"}, status=status.HTTP_404_NOT_FOUND
            )
        res = ShowCurrentUser().get(request)
        if res.status_code != 200:
            return Response(
                {"error": "User not found"}, status=status.HTTP_404_NOT_FOUND
            )

        user = User.objects.get(id=res.data["id"])

        if user != message.user:
            return Response(
                {"error": "Unauthorized action"}, status=status.HTTP_403_FORBIDDEN
            )

        serializer = MessageSerializer(message, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "Message updated", "data": serializer.data},
                status=status.HTTP_200_OK,
            )
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # delete message
    def delete(self, request, pk):
        try:
            message = Messages.objects.get(id=pk)
        except Messages.DoesNotExist:
            return Response(
                {"error": "Message not found"}, status=status.HTTP_404_NOT_FOUND
            )
        res = ShowCurrentUser().get(request)
        if res.status_code != 200:
            return Response(
                {"error": "User not found"}, status=status.HTTP_404_NOT_FOUND
            )

        user = User.objects.get(id=res.data["id"])

        if user != message.user:
            return Response(
                {"error": "Unauthorized action"}, status=status.HTTP_403_FORBIDDEN
            )

        message.delete()
        return Response({"message": "Message deleted"}, status=status.HTTP_200_OK)


class TopicsPageView(APIView):
    def get(self, request):
        q = request.GET.get("q") if request.GET.get("q") else ""
        topics = Topic.objects.filter(name__icontains=q)
        return Response(
            TopicSerializer(topics, many=True).data, status=status.HTTP_200_OK
        )


class ActivityPageView(APIView):
    def get(self, request):
        room_messages = Messages.objects.all()
        return Response(
            MessageSerializer(room_messages, many=True).data, status=status.HTTP_200_OK
        )
