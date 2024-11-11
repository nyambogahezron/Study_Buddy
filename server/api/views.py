from rest_framework import generics
from .models import Item
from .serializers import ItemSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import authenticate, login, logout
from django.db.models import Q
from .models import Room, Topic, Messages, User
from rest_framework import status
from .serializers import RoomSerializer, UserSerializer, MessageSerializer, TopicSerializer


class LoginPageView(APIView):
    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return Response(
                {"error": "Invalid details"}, status=status.HTTP_404_NOT_FOUND
            )

        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return Response({"message": "Login successful"}, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Invalid details"}, status=status.HTTP_400_BAD_REQUEST)


class LogoutUserView(APIView):
    def post(self, request):
        logout(request)
        return Response({"message": "Logout successful"}, status=status.HTTP_200_OK)


class RegisterUserView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()  
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return Response({"message": "Registration successful"}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class HomeView(APIView):
    def get(self, request):
        q = request.GET.get("q") if request.GET.get("q") else ""
        rooms = Room.objects.filter(
            Q(topic__name__icontains=q) | Q(name__icontains=q) | Q(description__icontains=q)
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
            return Response({"error": "You are not allowed here"}, status=status.HTTP_403_FORBIDDEN)

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
            return Response({"error": "You are not allowed here"}, status=status.HTTP_403_FORBIDDEN)

        room.delete()
        return Response({"message": "Room deleted"}, status=status.HTTP_200_OK)


class DeleteMessageView(APIView):
    def post(self, request, pk):
        message = Messages.objects.get(id=pk)
        if request.user != message.user:
            return Response({"error": "You are not allowed here"}, status=status.HTTP_403_FORBIDDEN)

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
        return Response(TopicSerializer(topics, many=True).data, status=status.HTTP_200_OK)


class ActivityPageView(APIView):
    def get(self, request):
        room_messages = Messages.objects.all()
        return Response(MessageSerializer(room_messages, many=True).data, status=status.HTTP_200_OK)


class ItemListCreateView(generics.ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class ItemDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
