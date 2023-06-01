from django.db import models
from django.utils.html import format_html

# Create your models here.
class categories(models.Model):
    cat_id=models.IntegerField(unique=True)
    cat_name = models.CharField(max_length=50)
    cat_desc = models.CharField(max_length=200)
    img = models.ImageField(upload_to='category_image/')
    def img_return(self):
        return format_html('<img src="/media/{}" style="width:40px; height:40px border-radius:70%" />'.format(self.img))
    
    def __str__(self):
        return self.cat_name
    


class products(models.Model):
    brand_name = models.CharField(max_length=110, null=True)
    pro_id=models.IntegerField(null=True,unique=True)
    pro_name = models.CharField(max_length=200)
    Pro_Description = models.CharField(max_length=2000, default='Default description')
    size = models.IntegerField(null=True)
    
    pro_cat = models.ForeignKey(categories, on_delete=models.CASCADE, related_name='products', default='product')
    price = models.IntegerField()
    img = models.ImageField(upload_to='ProductImage',null=True, blank=True)
    
    def __str__(self):
        return self.title
    
class contact(models.Model):
    
    name=models.CharField(max_length=50)
    contact_no=models.IntegerField()
    Email=models.CharField(max_length=20)
    subject=models.CharField(max_length=25)
    message=models.TextField(max_length=200)
    