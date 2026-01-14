from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status, generics, viewsets
from .models import Category, Product
from rest_framework.permissions import IsAuthenticated
from .permissions import CanUpdateWithin4Hours
from .serializers import ParentCategoryModelSerializer, ProductSerializer

# Create your views here.
 
class ParentCategoryListAPIView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = ParentCategoryModelSerializer 
    
    def get_queryset(self):
        queryset = Category.objects.filter(parent__isnull = True)
        return queryset
    

class ChildrenCategoryByCategorySlug(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = ParentCategoryModelSerializer
    
        
    def get_queryset(self):
        category_slug = self.kwargs['slug']
        parent = Category.objects.filter(slug =category_slug).first()
        if not parent:
            return Category.objects.none()
        return parent.children.all()
    
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated, CanUpdateWithin4Hours]

class ProductListByChildCategorySlug(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        slug = self.kwargs['slug']
        parent_category = Category.objects.filter(slug=slug).first()
        if not parent_category:
            return Product.objects.none()
        child_categories = parent_category.children.all()
        return Product.objects.filter(category__in=child_categories)
    
    
    
