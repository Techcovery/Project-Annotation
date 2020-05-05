from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Coordinates
from .serializers import CoordinateSerializer


class CoordinatesView(APIView):
    def get(self, request, pk=None):
        if pk:
            coordinates = get_object_or_404(Coordinates.objects.all(), pk=pk)
            serializer = CoordinateSerializer(coordinates)
            return Response({"coordinates": serializer.data})
        else:
            coordinates = Coordinates.objects.all()
            serializer = CoordinateSerializer(coordinates, many=True)
            return Response({"coordinates": serializer.data})

    def post(self, request):
        coordinates = request.data.get("coordinates")

        # Create an article from the above data
        serializer = CoordinateSerializer(data=coordinates)
        if serializer.is_valid(raise_exception=True):
            coordinates_saved = serializer.save()
        return Response({"success": "Coordinates '{}' created successfully".format((coordinates_saved.cur_moux , coordinates_saved.cur_mouy, coordinates_saved.las_moux , coordinates_saved.las_mouy))})

    # def put(self, request, pk):
    #     saved_article = get_object_or_404(Article.objects.all(), pk=pk)
    #     data = request.data.get('article')
    #     serializer = ArticleSerializer(instance=saved_article, data=data, partial=True)
    #
    #     if serializer.is_valid(raise_exception=True):
    #         article_saved = serializer.save()
    #     return Response({"success": "Article '{}' updated successfully".format(article_saved.title)})
    #
    #
    # def delete(self, request, pk):
    #     # Get object with this pk
    #     article = get_object_or_404(Article.objects.all(), pk=pk)
    #     article.delete()
    #     return Response({"message": "Article with id `{}` has been deleted.".format(pk)},status=204)
