from rest_framework.decorators import api_view
from rest_framework.response import Response
from base.models import Article
from .serializers import ArticleSerializer


@api_view(['GET'])
def getRoutes(request):
    routes = [
        'GET /api/',
        'GET /api/articles',
        'GET /api/articles/:id',
    ]
    return Response(routes)


@api_view(['GET'])
def getArticles(request):
    articles = Article.objects.all()
    serializer = ArticleSerializer(articles, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getArticle(request, pk):
    article = Article.objects.get(id=pk)
    serializer = ArticleSerializer(article, many=False)
    return Response(serializer.data)