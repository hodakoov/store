from rest_framework import serializers

from products.models import Product, ProductCategory


class ProductSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(
        queryset=ProductCategory.objects.all(),
        slug_field='name'
    )

    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'price', 'quantity', 'image', 'category',)
