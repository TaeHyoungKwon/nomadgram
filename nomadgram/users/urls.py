from django.urls import path

from nomadgram.users.views import (
    ExplorerUsers,
    FollowUser,
    UnFollowUser,
    UserProfile,
    UserFollowers,
    UserFollowing,
    Search
)

app_name = "users"
urlpatterns = [
    path("explore/", view=ExplorerUsers.as_view(), name="user_list"),
    path("search/", view=Search.as_view(), name="search"),
    path("<int:user_id>/follow/", view=FollowUser.as_view(), name="follow_user"),
    path("<int:user_id>/unfollow/", view=UnFollowUser.as_view(), name="unfollow_user"),
    path("<str:username>/", view=UserProfile.as_view(), name="user_profile"),
    path("<str:username>/followers/", view=UserFollowers.as_view(), name="user_followers"),
    path("<str:username>/following/", view=UserFollowing.as_view(), name="user_following"),

]
