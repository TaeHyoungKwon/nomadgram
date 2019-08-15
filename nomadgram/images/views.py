from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Image, Comment, Like
from .serializers import ImageSerializer, CommentSerializer, LikeSerializer


class Feed(APIView):
    def get(self, request, format=None):
        user = request.user
        following_users = user.following.all()
        image_list = []

        for following_user in following_users:
            user_images = list(following_user.image_set.all()[:2])

            for image in user_images:
                image_list.append(image)

        sorted_list = sorted(image_list, key=lambda image: image.created_at, reverse=True)
        serializer = ImageSerializer(sorted_list, many=True)


        return Response(serializer.data)
