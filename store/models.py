from django.db import models
from register.models import Profile
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
    

class Cart(models.Model):
    id=models.AutoField
    user=models.OneToOneField(Profile,on_delete=models.CASCADE)
    
    
    def getTotalPrice(self):
        sum = 0
        cartitems=CartItem.objects.filter(cart=self)
        print(cartitems)
        for cartitem in cartitems:
            sum+=cartitem.product.price*cartitem.quantity
        return sum
            
        
    
class CartItem(models.Model):
    cart=models.ForeignKey(Cart,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.SmallIntegerField(default=1)  
    
    
    
        
    
    
    

    

    