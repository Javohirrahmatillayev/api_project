from django.db import models

# Create your models here.

# class Car(models.Model):
#     name = models.CharField(max_length=100)
#     color = models.CharField(max_length=100)
#     year = models.IntegerField()
#     price = models.DecimalField(max_digits=14, decimal_places=2)

class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    parent = models.ForeignKey( 
        'self',
        related_name='children',
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        if self.parent:
            return f"{self.parent.title} -> {self.title}"
        return self.title       
    
    class Meta:
        verbose_name_plural = 'categories'
        
        
class Product(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(
        Category,
        related_name='products',
        on_delete=models.CASCADE
    )
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
    
class ProductImage(models.Model):
    product = models.ForeignKey(
        Product,
        related_name='images',
        on_delete=models.CASCADE
    )
    image = models.ImageField(upload_to='products/')
    is_main = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.product.name} image"