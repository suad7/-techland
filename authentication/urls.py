from django.urls import path
from .views import LoginView,register_view, ProfileList,ProfileDetails

urlpatterns =[
    path('login/', LoginView.as_view(), name='login'),
    path('register/', register_view, name='register'),
    path('api/profiles/', ProfileList.as_view()),
    path('api/profile/<int:pk>/', ProfileDetails.as_view())
]
