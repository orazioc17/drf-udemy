from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from posts.models import Post


class PostApiView(APIView):
    """
    Primera API creada con DRF
    """
    def get(self, request):
        """
        Funcion get para cuando se aplique el metodo get a la api
        """
        # posts = Post.objects.all()
        posts = {post.title: post.description for post in Post.objects.all()}
        return Response(status=status.HTTP_200_OK, data=posts)

    def post(self, request):
        """
        Funcion POST para cuando se aplique post a la api, guarda un nuevo Post de blog
        """
        Post.objects.create(
            title=request.POST['title'],
            description=request.POST['description'],
            order=request.POST['order'])
        return self.get(request)
