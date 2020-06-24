from rest_framework import serializers
from rest_framework.serializers import ModelSerializer,SerializerMethodField,ValidationError
from .models import Post
from django.contrib.auth import get_user_model
from comment.models import Comment
from comment.api.serializers import CommentSerializer




User = get_user_model()

# def create_comment_serializer(model_type='post', post_id=None, parent_id=None, author = None):
#     class CommentCreateSerializer(ModelSerializer):
#         class Meta:
#             model = Comment
#             fields = [
#                 'id',
#                 'parent',
#                 'content',
#                 'created',
#                 'author'
#             ]
#         def __init__(self, *args, **kwargs):
#             self.post_id=post_id
#             self.parent_obj = None
#             if parent_id:
#                 parent_qs = Comment.objects.filter(id=parent_id)
#                 if parent_qs.exists() and parent_qs.count() == 1:
#                     self.parent_obj =parent_qs.first()
#             return super(CommentCreateSerializer, self).__init__(*args, **kwargs)


#         def validate(self, data):
#             obj_qs = Comment.objects.filter(post_id = self.post_id)
#             if not obj_qs.exists() or obj_qs.count() != 1:
#                 raise ValidationError('This is not a valid id')
#             return data

#         def create(self, validated_data):
#             content = validated_data.get('content')
#             if author:
#                 main_author = User
#             else:
#                 main_author = User.objects.all().first()
#             post_id = self.post_id
#             parent_obj = self.parent_obj
#             comment = Comment.objects.create_comment(post_id,content, main_author,parent_obj=parent_obj)
#             return Comment
#     return CommentCreateSerializer






# class CommentSerializer(ModelSerializer):
#     reply_count = SerializerMethodField()
#     class Meta:
#         model = Comment
#         fields = [
#             'id',
#             'post',
#             'content',
#             'created',
#             'author',
#             'parent',
#             'reply_count'
#         ]

#     def get_reply_count(self, obj):
#         if obj.is_parent:
#             return obj.children().count()
#         return 0

# class CommentChildSerializer(ModelSerializer):
#     class Meta:
#         model = Comment
#         fields = [
#             'id',
#             'content',
#             'created',
#             'author',
#         ]


# class CommentDetailSerializer(ModelSerializer):
#     replies = SerializerMethodField()
#     reply_count = SerializerMethodField()

#     class Meta:
#         model = Comment
#         fields = [
#             'id',
#             'post',
#             'content',
#             'author',
#             'replies',
#             'reply_count',
#             'created'
#         ]
#     def get_replies(self, obj):
#         if obj.is_parent:
#             return CommentChildSerializer(obj.children(), many=True).data
#         return None


#     def get_reply_count(self, obj):
#         if obj.is_parent:
#             return obj.children().count()
#         return 0


class PostSerializer(serializers.ModelSerializer):
    comments = SerializerMethodField()
    class Meta:
        model = Post
        fields = ('id','image', 'title', 'content', 'timestamp', 'category', 'author', 'comments')

    # def create(self,validated_data):
    #     return Post.objects.create(**validated_data)

    def get_comments(self, obj):
        # object_id = obj.id
        comments_qs = Comment.objects.filter_parents_by_object(obj)
        return CommentSerializer(comments_qs, many=True).data
