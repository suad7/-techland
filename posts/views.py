from django.shortcuts import render
from rest_framework.generics import (
    CreateAPIView,
    DestroyAPIView,
    ListAPIView,
    UpdateAPIView,
    RetrieveAPIView,
    RetrieveUpdateAPIView
    )
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly
    )
from .serializer import CommentSerializer,CommentDetailSerializer
from .models import Comment, Post
from authentication.models import User



class CommentDetailView(RetrieveAPIView):
    queryset= Comment.objects.all()
    serializer_class = CommentDetailSerializer


class CommentListView(ListAPIView):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
