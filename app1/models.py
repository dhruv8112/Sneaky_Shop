from django.db import models
from django.utils.html import format_html

# Create your models here.


class products(models.Model):
    brand_name = models.CharField(max_length=110, null=True)
    pro_id=models.IntegerField(null=True,unique=True)
    pro_name = models.CharField(max_length=200)
    Pro_Description = models.CharField(max_length=2000, default='Default description')
    size = models.IntegerField(null=True)
    # pro_cat = models.ForeignKey(categories, on_delete=models.CASCADE, related_name='products')
    price = models.IntegerField()
    img = models.ImageField(upload_to='ProductImage',null=True, blank=True)
    
    
class contact(models.Model):
    
    name=models.CharField(max_length=50)
    contact_no=models.IntegerField()
    Email=models.CharField(max_length=20)
    subject=models.CharField(max_length=25)
    message=models.TextField(max_length=200)
    