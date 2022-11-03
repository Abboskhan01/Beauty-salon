from rest_framework import serializers
from .models import Category, Cosmetic


class CosmeticSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cosmetic
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
