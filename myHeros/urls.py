from django.urls import path, include
from rest_framework import routers
from . import views

# app_name = 'myHeros'

router = routers.DefaultRouter()
router.register('myHeros', views.HeroViewSet)
urlpatterns = [
    path('', views.home, name='home'),
    path('myHero', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
