from django.shortcuts import redirect
from .serializers import BlogSerializers
from blog.models import Post
from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly
from blog.api.pagination import MyPagination
class BlogAPI(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = BlogSerializers
    authentication_classes = [TokenAuthentication,]
    permission_classes = [IsAuthenticatedOrReadOnly,]
    pagination_class = MyPagination



