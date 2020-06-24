from rest_framework import serializers
from rest_framework.serializers import ModelSerializer,SerializerMethodField,ValidationError
from .models import Post
from django.contrib.auth import get_user_model
from comment.models import Comment
from comment.api.serializers import CommentSerializer




User = get_user_model()



class PostSerializer(serializers.ModelSerializer):
    comments = SerializerMethodField()
    class Meta:
        model = Post
        fields = ('id','image', 'title', 'content', 'timestamp', 'category', 'author', 'comments')

   

    def get_comments(self, obj):
        comments_qs = Comment.objects.filter_parents_by_object(obj)
        return CommentSerializer(comments_qs, many=True).data
