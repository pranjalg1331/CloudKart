from django.db import models

# Create your models here.
class Category(models.Model):
    id=models.AutoField
    name=models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
    
    
class Product(models.Model):
    id=models.AutoField
    name = models.CharField(max_length=100)
    price = models.IntegerField(default=0)
    category=models.ForeignKey(Category,on_delete=models.CASCADE,default="")
    image=models.ImageField(upload_to='products/')
    
    def __str__(self) :
        return self.name
    
    def products_bycategory(id):
        return Product.objects.filter(category=id)

    
    