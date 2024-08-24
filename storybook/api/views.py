from django.shortcuts import render
from rest_framework import viewsets
from .models import Story, Page
from .serializers import StorySerializer, PageSerializer

class StoryViewSet(viewsets.ModelViewSet):
    queryset = Story.objects.all()
    serializer_class = StorySerializer

class PageViewSet(viewsets.ModelViewSet):
    queryset = Page.objects.all()
    serializer_class = PageSerializer
    
def index(request):
    return render(request, 'index.html')