import os
import yaml
from django.urls import path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from django.urls import path
from .views import (
    HomeView,
    LoginPageView,
    LogoutUserView,
    RegisterUserView,
    RoomView,
    UserProfileView,
    CreateRoomView,
    UpdateRoomView,
    DeleteRoomView,
    UpdateUserView,
    TopicsPageView,
    ActivityPageView,
    ShowCurrentUser,
    GetAllRoomsView,
    SendMessageView,
    MessageActionsView,
)


# Load YAML file
with open(os.path.join(os.path.dirname(__file__), "docs.yaml"), "r") as file:
    schema_dict = yaml.safe_load(file)

# Create SchemaView from YAML
schema_view = get_schema_view(
    openapi.Info(
        title=schema_dict["info"]["title"],
        default_version=schema_dict["info"]["version"],
        description=schema_dict["info"]["description"],
    ),
    public=True,
)

urlpatterns = [
    # auth routes
    path("login/", LoginPageView.as_view(), name="login"),
    path("logout/", LogoutUserView.as_view(), name="logout"),
    path("register/", RegisterUserView.as_view(), name="register"),
    # user routes
    path("current_user/", ShowCurrentUser.as_view(), name="current_user"),
    path("user/update/", UpdateUserView.as_view(), name="update-user"),
    path("profile/<int:pk>/", UserProfileView.as_view(), name="user-profile"),
    # room routes
    path("rooms/create/", CreateRoomView.as_view(), name="create-room"),
    path("rooms/", GetAllRoomsView.as_view(), name="get-all-rooms"),
    path("room/<int:pk>/", RoomView.as_view(), name="room"),
    path("rooms/update/<int:pk>/", UpdateRoomView.as_view(), name="update-room"),
    path("rooms/delete/<int:pk>/", DeleteRoomView.as_view(), name="delete-room"),
    # message routes
    path("message/send/<int:pk>/", SendMessageView.as_view(), name="messages"),
    path("message/<int:pk>/", MessageActionsView.as_view(), name="messages"),
    # topics routes
    path("topics/", TopicsPageView.as_view(), name="topics"),
    # activity routes
    path("activity/", ActivityPageView.as_view(), name="activity"),
    # other route
    path("", HomeView.as_view(), name="home"),
    # documentation routes
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
]
