from rest_framework import serializers
from rest_framework.serializers import ModelSerializer,SerializerMethodField
from .models import Post,Comment



class CommentSerializer(ModelSerializer):
    reply_count = SerializerMethodField()
    class Meta:
        model = Comment
        fields = [
            'id',
            'post',
            'content',
            'created',
            'author',
            'parent',
            'reply_count'
        ]

    def get_reply_count(self, obj):
        if obj.is_parent:
            return obj.children().count()
        return 0

class CommentChildSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = [
            'id',
            'content',
            'created',
            'author',
        ]


class CommentDetailSerializer(ModelSerializer):
    replies = SerializerMethodField()
    reply_count = SerializerMethodField()

    class Meta:
        model = Comment
        fields = [
            'id',
            'post',
            'content',
            'author',
            'replies',
            'reply_count',
            'created'
        ]
    def get_replies(self, obj):
        if obj.is_parent:
            return CommentChildSerializer(obj.children(), many=True).data
        return None


    def get_reply_count(self, obj):
        if obj.is_parent:
            return obj.children().count()
        return 0