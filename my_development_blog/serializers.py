from rest_framework import serializers

from .models import Post


class PostsSerializer(serializers.ModelSerializer):
    model = Post
    fields = '__all__'
