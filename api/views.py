from rest_framework.viewsets import ModelViewSet
from .models import Cosmetic, Category
from .serializers import CategorySerializer, CosmeticSerializer


class CosmeticViewSet(ModelViewSet):
    queryset = Cosmetic.objects.all()
    serializer_class = CosmeticSerializer


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
