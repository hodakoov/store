from rest_framework import serializers

from products.models import Product, ProductCategory, Baskets


class ProductSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(
        queryset=ProductCategory.objects.all(),
        slug_field='name'
    )

    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'price', 'quantity', 'image', 'category',)


class BasketSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    sum = serializers.FloatField()
    total_sum = serializers.SerializerMethodField()
    total_quantity = serializers.SerializerMethodField()

    class Meta:
        model = Baskets
        fields = ('id', 'product', 'quantity', 'sum', 'total_sum', 'total_quantity', 'created_timestamp',)
        read_only_fields = ('created_timestamp',)

    def get_total_sum(self, obj):
        return Baskets.objects.filter(user_id=obj.user.id).total_sum()

    def get_total_quantity(self, obj):
        return Baskets.objects.filter(user_id=obj.user.id).total_quantity()
