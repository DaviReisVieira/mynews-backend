from django.shortcuts import render
import json
from django.http import JsonResponse
from rest_framework.views import APIView
import requests

from mynewsauth.models import CustomUserModel
from news.models import StoredNews
# Create your views here.

class NewsListView(APIView):
  def get(self, request, *args, **kwargs):
    news = requests.get("https://newsapi.org/v2/top-headlines?country=br&apiKey=4475954939f346ac80770d030097579c")
    content = news.content
    stringified = json.loads(content)
    return JsonResponse(stringified, safe=False)

class StoredNewsListView(APIView):
  def get(self, request, *args, **kwargs):
    news = StoredNews.objects.filter(user=request.user)

    return JsonResponse({'news': [{'title': n.title, 'content': (n.content)} for n in news]})

  def post(self, request, *args, **kwargs):
    jsonBody = json.loads(request.body)
    print(jsonBody['content']['source'])
    news, create = StoredNews.objects.get_or_create(
      content=jsonBody['content'],
      user=request.user,
      title=jsonBody['content']['title']
      )
    
    if create:
      news.save()

    return JsonResponse({'created': str(create)})

  def delete(self, request, *args, **kwargs):
    jsonBody = json.loads(request.body)

    news = StoredNews.objects.get(title=str(jsonBody['content']['title']))
    news.delete()

    return JsonResponse({'deleted': 'ok'})
