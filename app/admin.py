from django.contrib import admin
from .models import Category, Product, ProductImage
# Register your models here.


@admin.register(Category)
class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    prepopulated_fields = {'slug':('title',)}
    
class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'is_active', 'created_at')
    prepopulated_fields = {'slug': ('name',)} 
    list_filter = ('is_active', 'category')
    inlines = [ProductImageInline]

    
