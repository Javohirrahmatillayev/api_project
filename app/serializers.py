from rest_framework import serializers
from .models import Category, Product

class ParentCategoryModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        exclude = ()
        


class ProductSerializer(serializers.ModelSerializer):
    category = ParentCategoryModelSerializer(read_only=True)  
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(),
        source='category',
        write_only=True 
    )

    class Meta:
        model = Product
        fields = [
            'id', 'name', 'slug', 'description', 'price',
            'category', 'category_id', 'image', 'is_active',
            'created_at', 'updated_at'
        ]