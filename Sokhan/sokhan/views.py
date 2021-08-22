from django.contrib.auth import get_user_model
from rest_framework.generics import CreateAPIView, DestroyAPIView, ListAPIView, get_object_or_404
from rest_framework.permissions import IsAuthenticated

from sokhan.models import Post
from sokhan.permissions import IsClient, IsAdmin
from sokhan.serializers import CreatePostSerializer, ProfilePostSerializer, UserPostSerializer

User = get_user_model()


class CreatePostAPIView(CreateAPIView):
    serializer_class = CreatePostSerializer
    permission_classes = [IsAuthenticated, IsClient]


class DeletePostAPIView(DestroyAPIView):
    queryset = Post.objects.all()
    permission_classes = [IsAuthenticated, IsAdmin]
    lookup_field = 'pk'


class ListPostsByUserAPIView(ListAPIView):
    serializer_class = ProfilePostSerializer

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs['username'])
        return user.post_set.all()


class ListAllPostsView(ListAPIView):
    serializer_class = UserPostSerializer
    queryset = Post.objects.all()
