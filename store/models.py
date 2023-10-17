from django.db import models
from register.models import Profile
import datetime
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
    
    def getCouponDiscountedPrice(self,value):
        totalprice=Cart.getTotalPrice(self)
        totalprice=totalprice-(totalprice*(value/100))
        return totalprice
            
        
    
class CartItem(models.Model):
    cart=models.ForeignKey(Cart,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.SmallIntegerField(default=1)
    
  
class Coupan(models.Model):
    code=models.CharField(max_length=20)
    value=models.SmallIntegerField(default=0)
    expiry_date=models.DateField(auto_now=True)
    
    def save(self, *args, **kwargs):
        
        self.expiry_date = datetime.date.today() + datetime.timedelta(days=2)
        super(Coupan, self).save(*args, **kwargs)
        
class Order(models.Model):
    cart=models.OneToOneField(Cart,on_delete=models.PROTECT)
    final_price=models.IntegerField(default=0)
    
    
    
    
    
    
    

    

    