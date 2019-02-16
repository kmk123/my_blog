from rest_framework.serializers import ModelSerializer
from blog.models import Post

class BlogSerializers(ModelSerializer):
    class Meta:
        model=Post
        fields='__all__'

