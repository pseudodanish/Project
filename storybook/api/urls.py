from django.urls import include, path
from rest_framework import routers
from .views import StoryViewSet, PageViewSet , index

router = routers.DefaultRouter()
router.register(r'stories', StoryViewSet)
router.register(r'pages', PageViewSet)

urlpatterns = [
    path('', index, name='index'),
    path('api/', include(router.urls)),
]
