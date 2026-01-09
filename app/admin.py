from django.contrib import admin
from .models import Category, Product
# Register your models here.


@admin.register(Category)
class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    prepopulated_fields = {'slug':('title',)}
    
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'is_active', 'created_at')
    prepopulated_fields = {'slug': ('name',)} 
    list_filter = ('is_active', 'category')
