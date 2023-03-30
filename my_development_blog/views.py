from django.shortcuts import render
from django.views import View
from rest_framework.generics import ListAPIView, RetrieveAPIView
from .models import Post
from .serializers import PostsSerializer


class PostsListView(ListAPIView):

    def get_queryset(self):
        return Post.objects.published_posts()

    serializer_class = PostsSerializer
    pagination_class = None


class PostsView(RetrieveAPIView):

    def get_queryset(self):
        return Post.objects.published_posts()

    serializer_class = PostsSerializer


class MainView(View):

    def get(self, request):
        # posts = PostsView.get_queryset()

        # context = {'posts': posts}
        return render(request, '')

    # def post(self, request):
    #
    #     context = {}
    #     return render(request, '', context=context)
