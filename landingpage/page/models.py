from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class OrderModel(models.Model):
    
    name = models.CharField(max_length=50, default='Nothing')
    phone = models.CharField(max_length=14, default='Nothing')
    address = models.CharField(max_length=200,default='Nothing')
    comment = models.TextField(null=True, blank=True, default='Nothing')
    quantity = models.CharField( default='Nothing')
    
    statusChoice = [
        ('Pending','Pending'),
        ('Submit','Submit'),
        ('Done','Done'),
        ('Cancel', 'Cancel')
    ]
    status = models.CharField(choices=statusChoice, default="Pending" ,null=True)
    
    locationChoice = [
        ("ID" , "Inside Dhaka"),
        ("OD" , "Outside Dhaka"),
    ]
    
    product_name = models.CharField(max_length=250, default='Nothing')
    price = models.CharField(default=0)
    delivery_charge = models.CharField(default=0)
    total_price = models.CharField(default=0)
    
    paymentChoice = [
        ("CD", "Cash on Delivary" ),
        ("OP" , "Online Payment"),
    ]
    payment_method = models.CharField(choices=paymentChoice, max_length=60, default='Nothing')
    transaction_method = models.CharField(max_length=100, default='Nothing')
    transaction_id = models.CharField(default='Nothing')
    
    location_choice = models.CharField( choices=locationChoice, default="Inside Dhaka")
    

    
    order_created_at = models.DateTimeField(auto_now= True)
    order_updated_at = models.DateTimeField( auto_now_add=True)
    
    def __str__(self):
        return f'{self.name}'
    

class FontSection(models.Model):
    name = models.CharField(max_length=20)
    small_title = models.CharField(null=True, blank=True)
    big_title = models.CharField()
    font_asset = models.ImageField(upload_to='font_asset/', default="not-found.jpg")
    details = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return f'{self.name}'
    
class FeatureSection(models.Model):
    name = models.CharField(max_length=20)
    first_title = models.CharField(null=True, blank=True)
    features_name = models.JSONField(default=list, blank=True)
    second_title = models.CharField(null=True, blank=True)
    benefits_name = models.JSONField(default=list, blank=True)
    
    def __str__(self):
        return f'{self.name}'
    

class ContactSection(models.Model):
    title = models.CharField()
    number= models.CharField(unique=True)
    
    def __str__(self):
        return f"{self.title}"
    
class Photo(models.Model):
    name = models.CharField(blank=True)
    photo_asset = models.ImageField(upload_to='photo_asset/', default="not-found.jpg", null=True, blank=True)
    
    def __str__(self):
        return f"{self.name}"
    
class GellerySection(models.Model):
    title = models.CharField()
    description = models.TextField(blank=True)
    photos = models.ManyToManyField(Photo, related_name='gellery', blank=True)
    
    def __str__(self):
        return f"{self.title}"
    
class ProductDetails(models.Model):
    name = models.CharField()
    quantity = models.CharField(default=0)
    price = models.CharField(default=0) # product price
    insideDhaka = models.CharField(default=0) # Delivery inside Dhaka
    outsideDhaka = models.CharField(default=0) # Delivery outside Dhaka
    
    def __str__(self):
        return f"{self.name}"
           
    
    
    
    
    
    