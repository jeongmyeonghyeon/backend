from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer): # ViewSet은 CRUD가 모두 들어간 API를 만들어 주쥬?
    class Meta:
        model = Post
        fields = '__all__' # 작성자 같은거 빼야하지만 일단 이렇게
