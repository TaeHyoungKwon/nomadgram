from django.urls import path
from . import views

app_name = "images"
urlpatterns = [
    path("",
         view=views.Feed.as_view(),
         name="all_images"
    ),
    path("search/",
         view=views.Search.as_view(),
         name="search"
    ),

    ]
