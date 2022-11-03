from rest_framework import routers
from .views import CosmeticViewSet, CategoryViewSet
from django.urls import path, include

router = routers.DefaultRouter()
router.register(r'cosmetic', CosmeticViewSet)
router.register(r'category', CategoryViewSet)

urlpatterns = [
    path('', include(router.urls))
]
