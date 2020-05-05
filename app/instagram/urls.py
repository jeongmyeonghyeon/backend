from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('posts', views.PostViewSet) # DefaultRouter & .register -> 낯설다 (자동으로 만들어주는 부분 포함)

urlpatterns = [
    path('api/', include(router.urls)),
]