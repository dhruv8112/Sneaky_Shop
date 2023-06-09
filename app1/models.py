from django.db import models
from django.utils.html import format_html
from django.contrib.auth.models import User

# Create your models here.


class categories(models.Model):
    cat_id = models.IntegerField(unique=True)
    cat_name = models.CharField(max_length=50)
    cat_desc = models.CharField(max_length=200)
    img = models.ImageField(upload_to='category_image/')

    def img_return(self):
        return format_html('<img src="/media/{}" style="width:40px; height:40px border-radius:70%" />'.format(self.img))

    def __str__(self):
        return self.cat_name


class products(models.Model):
    brand_name = models.CharField(max_length=110, null=True)
    pro_id = models.IntegerField(null=True, unique=True)
    pro_name = models.CharField(max_length=200)
    Pro_Description = models.CharField(
        max_length=2000, default='Default description')
    size = models.IntegerField(null=True)

    pro_cat = models.ForeignKey(
        categories, on_delete=models.CASCADE, related_name='products', default='product')
    price = models.IntegerField()
    img = models.ImageField(upload_to='ProductImage', null=True, blank=True)


class contact(models.Model):

    name = models.CharField(max_length=50)
    contact_no = models.IntegerField()
    Email = models.CharField(max_length=20)
    subject = models.CharField(max_length=25)
    message = models.TextField(max_length=200)


class Cart(models.Model):
    cart_id=models.IntegerField(default=1)
    product_id = models.IntegerField()
    quantity = models.IntegerField()
    total_price = models.IntegerField()
    cart_product_name = models.CharField(
        max_length=100, default="Not get Product")
    cart_img=models.ImageField(upload_to='cart_product',null=True)

    def __str__(self):
        return self.cart_product_name


class user_info(models.Model):
    usernmae = models.CharField(max_length=50)
    # contact_no = models.IntegerField()
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    email=models.CharField(max_length=50)
    password = models.CharField(max_length=40)




class order_details(models.Model):
    order_id=models.CharField(max_length=100)
    user_name=models.CharField(max_length=100)
    user_email=models.CharField(max_length=100)
    product_name=models.CharField(max_length=100)
    total=models.IntegerField()
    payment_mode=models.CharField(max_length=50)
    address=models.CharField(max_length=100)
    pincode=models.CharField(max_length=10)
    phone_no=models.CharField(max_length=100)
    country=models.CharField(max_length=10)
    is_buy=models.BooleanField(default=False)
    shipping=models.TextField(default="No special shipping")