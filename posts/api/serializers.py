from rest_framework.serializers import ModelSerializer
from posts.models import Post


class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        # fields = '__all__' || Esto no es la mejor forma de hacerlo porque pueden haber veces que no queramos utilizar
        # todos los campos en una peticion
        fields = ['title', 'description', 'order', 'created_at']
