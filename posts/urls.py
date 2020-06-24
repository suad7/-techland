from django.urls import path,re_path
from . import views



urlpatterns = [
    path('api/posts/', views.PostList.as_view()),
    path('api/posts/<int:pk>', views.PostDetails.as_view()),

]

