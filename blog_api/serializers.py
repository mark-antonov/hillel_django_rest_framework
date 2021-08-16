from django.contrib.auth.models import User

from rest_framework import serializers

from .models import Comment, Post


class UserSerializer(serializers.HyperlinkedModelSerializer):
    posts = serializers.PrimaryKeyRelatedField(many=True, read_only=True)  # related_name
    comments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)  # related_name

    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'email', 'groups', 'is_staff', 'posts', 'comments']


class PostSerializer(serializers.HyperlinkedModelSerializer):
    # user = serializers.ReadOnlyField(source='user.username')
    user = UserSerializer(read_only=True)
    comments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)  # related_name

    class Meta:
        model = Post
        fields = ['url', 'id', 'title', 'user', 'short_description',
                  'full_description', 'created', 'posted', 'comments']


class CommentSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    # user = UserSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = ['url', 'id', 'text', 'user', 'post', 'created', 'moderated']
