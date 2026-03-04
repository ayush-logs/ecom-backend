from rest_framework import serializers
from .models import Category, Product


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name"]


class ProductSerializer(serializers.ModelSerializer):
    # TODO add logic to make category field write field

    # category = serializers.StringRelatedField()
    category = CategorySerializer(read_only=True)

    class Meta:
        model = Product
        fields = ("name", "category", "description", "price", "is_active")
 