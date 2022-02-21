from django.urls import path
from .views import *
urlpatterns = [
    path("", List.as_view()),
    path("api/<int:id>/", Post_Single_List.as_view()),
    path("add/", Post_List.as_view()),
    path("update/<int:id>/", Update_List.as_view()),
    path("delete/<int:id>/", Delete_List.as_view()),
]
