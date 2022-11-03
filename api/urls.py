from rest_framework import routers
from .views import CosmeticSerializer, CategorySerializer
from django.urls import path, include

router = routers.DefaultRouter()
router.register(r'cosmetic', CosmeticSerializer)
router.register(r'category', CategorySerializer)

urlpatterns = [
    path('', include(router.urls))
]
