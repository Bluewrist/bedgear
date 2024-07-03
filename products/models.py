from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from PIL import Image,ImageDraw,ImageFont
from users.models import CustomerUser

import uuid



    
class Type(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class product_category(models.Model):
    parent = models.ForeignKey('self', related_name='children', on_delete=models.CASCADE, blank = True, null=True)
    name =  models.CharField(max_length= 300,unique=True)
    category_description =  models.CharField(max_length= 1000)


    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=200)    
    price =  models.IntegerField(default= 0)
    product_detail =  models.TextField(max_length=1000)
    product_category =  models.ForeignKey(product_category,on_delete = models.CASCADE)
    product_img  =  models.ImageField(upload_to='cars',default='default.png')
    issued_to = models.CharField(max_length=200) 
    reorder_level = models.IntegerField(default=1)
    is_trending  =  models.BooleanField(default = False)
    on_sale =  models.BooleanField(default=False)
    is_new = models.BooleanField(default=False)
    date =  models.DateTimeField(auto_now_add=True)
    buying_price = models.IntegerField(default=1)
    qyt = models.IntegerField(default=1)
    last_updates= models.DateTimeField(auto_now_add=False,auto_now=True)


    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self):
        return reverse("product_detail",args=[self.id])    

  


class Product_images(models.Model):
    product_id = models.ForeignKey(Product,on_delete=models.CASCADE)
    product_img = models.ImageField(upload_to='cars',default='default-car.png') 

    def __str__(self) -> str:
        return self.product_id.name 




class Order(models.Model):
    customer = models.ForeignKey(CustomerUser,on_delete=models.SET_NULL,blank=True,null=True)
    date_orderd =  models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False) 
    transaction_id =  models.CharField(max_length=200,null=True)

    
    def __str__(self):
        return str(self.transaction_id)
    

    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total 

    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total


    @property
    def get_vat(self):
        total = self.get_cart_total
        vat = 15/100 * total
        return vat
    
    @property
    def grand_total(self):
        total = self.get_cart_total + self.get_vat
        return total

    @property
    def address(self):
        address = self.diliveryAddress_set.all()
        return address
    

class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL,blank=True,null=True)
    order = models.ForeignKey(Order, on_delete= models.SET_NULL,blank=True,null=True )
    quantity = models.IntegerField(default=0)
    date_orderd =  models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.product.part_name 

    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total
    

class DiliveryAddress(models.Model):
    customer = models.ForeignKey(CustomerUser,on_delete=models.SET_NULL,blank=True,null=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    first_name =  models.CharField(max_length=200,null=True,blank=True)
    last_name =  models.CharField(max_length=200,null=True,blank=True)
    phone =  models.CharField(max_length=200,null=True,blank=True)
    phone2 =  models.CharField(max_length=200,null=True,blank=True)
    city = models.CharField(max_length=200,null=True,blank=True)
    suburb =  models.CharField(max_length=200,null=True,blank=True)
    address = models.CharField(max_length=20,default='123 angwa harare')
    date_orderd =  models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address



class contact_us(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    telephone = models.CharField(max_length = 1000)
    comment = models.TextField(max_length=500)
    date =  models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Email(models.Model):
    name = models.CharField(max_length = 1000,default= "hhhdhdh")
    email = models.EmailField()
    date =  models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.email


class Search(models.Model):
    name = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now=True)
    ip_address = models.CharField(default='',max_length=200)
    users = models.CharField(default='',max_length=200)

    def __str__(self):
        return self.name

    


