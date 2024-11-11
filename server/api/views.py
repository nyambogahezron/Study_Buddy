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


class ShowCurrentUser(APIView):
    def get(self, request):
        token = request.COOKIES.get("access_token")
        if not token:
            return Response(
                {"error": "No token provided"}, status=status.HTTP_401_UNAUTHORIZED
            )

        try:
            # Verify the token and get the payload
            payload = UntypedToken(token)
            user_id = payload.get("user_id")
            if not user_id:
                return Response(
                    {"error": "Invalid token payload"},
                    status=status.HTTP_401_UNAUTHORIZED,
                )

            # Get the user from the database
            user = User.objects.get(id=user_id)
            return Response(UserSerializer(user).data, status=status.HTTP_200_OK)

        except (InvalidToken, TokenError) as e:
            return Response(
                {"error": "Unauthenticated"}, status=status.HTTP_401_UNAUTHORIZED
            )


class LogoutUserView(APIView):
    def post(self, request):
        logout(request)
        response = Response()
        response.delete_cookie("access_token")
        response.delete_cookie("refresh_token")
        return Response({"message": "Logout successful"}, status=status.HTTP_200_OK)


class RegisterUserView(APIView):
    def post(self, request):
        user = User.objects.filter(
            Q(email=request.data.get("email"))
            | Q(username=request.data.get("username"))
        )
        if user.exists():
            return Response(
                {"error": "Invalid credentials"},
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
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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


class UserProfileView(APIView):
    def get(self, request, pk):
        user = User.objects.get(id=pk)
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


class CreateRoomView(APIView):
    def post(self, request):
        topic_name = request.data.get("topic")
        topic, created = Topic.objects.get_or_create(name=topic_name)
        room_data = {
            "host": request.user.id,
            "topic": topic.id,
            "name": request.data.get("name"),
            "description": request.data.get("description"),
        }
        serializer = RoomSerializer(data=room_data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Room created"}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UpdateRoomView(APIView):
    def post(self, request, pk):
        room = Room.objects.get(id=pk)
        if request.user != room.host:
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
            return Response({"message": "Room updated"}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DeleteRoomView(APIView):
    def post(self, request, pk):
        room = Room.objects.get(id=pk)
        if request.user != room.host:
            return Response(
                {"error": "You are not allowed here"}, status=status.HTTP_403_FORBIDDEN
            )

        room.delete()
        return Response({"message": "Room deleted"}, status=status.HTTP_200_OK)


class DeleteMessageView(APIView):
    def post(self, request, pk):
        message = Messages.objects.get(id=pk)
        if request.user != message.user:
            return Response(
                {"error": "You are not allowed here"}, status=status.HTTP_403_FORBIDDEN
            )

        message.delete()
        return Response({"message": "Message deleted"}, status=status.HTTP_200_OK)


class UpdateUserView(APIView):
    def post(self, request):
        user = request.user
        serializer = UserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User updated"}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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


class ItemListCreateView(generics.ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class ItemDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
