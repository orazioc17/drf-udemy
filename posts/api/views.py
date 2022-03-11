from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from posts.models import Post
from posts.api.serializers import PostSerializer


class PostApiView(APIView):
    """
    Primera API creada con DRF
    """
    def get(self, request):
        """
        Funcion get para cuando se aplique el metodo get a la api
        """
        # posts = Post.objects.all()
        # posts = {post.title: post.description for post in Post.objects.all()}
        serializer = PostSerializer(Post.objects.all(), many=True)  # El many = True es para que devuelva el array
        # Completo de los posts
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    def post(self, request):
        """
        Funcion POST para cuando se aplique post a la api, guarda un nuevo Post de blog
        """
        # Post.objects.create(
        #    title=request.POST['title'],
        #    description=request.POST['description'],
        #    order=request.POST['order'])
        serializer = PostSerializer(data=request.POST)  # Con esto el serializador buscara los datos que tiene q buscar
        serializer.is_valid(raise_exception=True)  # Y con esto, si ocurre algun error o algun dato es invalido, elevara
        # una exception
        serializer.save()  # Y este save para guardar en la base de datos
        return Response(status=status.HTTP_200_OK, data=serializer.data)
