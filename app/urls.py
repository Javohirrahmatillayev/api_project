from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *


router = DefaultRouter()
router.register(r'apelsin.uz/products', ProductViewSet, basename='product')

urlpatterns = [
    path('apelsin.uz/', ParentCategoryListAPIView.as_view()),
    path('apelsin.uz/category/<slug:slug>/', ChildrenCategoryByCategorySlug.as_view()),
    
    path('apelsin.uz/products-by-category/<slug:slug>/', ProductListByChildCategorySlug.as_view(), name='products-by-child-category'),

    path('', include(router.urls)),
]
