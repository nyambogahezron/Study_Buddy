from django.urls import path
from .views import (
    ItemListCreateView, ItemDetailView, HomeView, LoginPageView, LogoutUserView, RegisterUserView,
    RoomView, UserProfileView, CreateRoomView, UpdateRoomView, DeleteRoomView, DeleteMessageView,
    UpdateUserView, TopicsPageView, ActivityPageView
)

urlpatterns = [
    path("items/", ItemListCreateView.as_view(), name="item-list-create"),
    path("items/<int:pk>/", ItemDetailView.as_view(), name="item-detail"),
    path("", HomeView.as_view(), name="home"),
    path("login/", LoginPageView.as_view(), name="login"),
    path("logout/", LogoutUserView.as_view(), name="logout"),
    path("register/", RegisterUserView.as_view(), name="register"),
    path("rooms/<int:pk>/", RoomView.as_view(), name="room"),
    path("profile/<int:pk>/", UserProfileView.as_view(), name="user-profile"),
    path("rooms/create/", CreateRoomView.as_view(), name="create-room"),
    path("rooms/update/<int:pk>/", UpdateRoomView.as_view(), name="update-room"),
    path("rooms/delete/<int:pk>/", DeleteRoomView.as_view(), name="delete-room"),
    path("messages/delete/<int:pk>/", DeleteMessageView.as_view(), name="delete-message"),
    path("user/update/", UpdateUserView.as_view(), name="update-user"),
    path("topics/", TopicsPageView.as_view(), name="topics"),
    path("activity/", ActivityPageView.as_view(), name="activity"),
]
