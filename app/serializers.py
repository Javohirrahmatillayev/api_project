from rest_framework import serializers
from .models import Category, Product, ProductImage


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ['id', 'image', 'is_main']

class ParentCategoryModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'title', 'slug']
        

class ProductSerializer(serializers.ModelSerializer):
    category = ParentCategoryModelSerializer(read_only=True)  
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(),
        source='category',
        write_only=True 
    )

    images = ProductImageSerializer(many = True, read_only = True)
    main_image = serializers.SerializerMethodField()
    
    
    class Meta:
        model = Product
        fields = [
            'id', 
            'name', 
            'slug', 
            'description', 
            'price',
            'category', 
            'category_id', 
            'images',
            'main_image', 
            'is_active',
            'created_at',
            'updated_at'
        ]
        
    def get_main_image(self, obj):
        image = obj.images.filter(is_main = True).first()
        return image.image.url if image else None