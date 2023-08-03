"""
URL configuration for Sneaky_Shop project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path
from app1.views import *
from django.contrib.auth.views import PasswordChangeView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('register/', register_page, name='register'),
    path('login', login, name='login'),
    path('contact_us', contact_us, name='contact_us'),
    path('single/<int:pro_id>/', single_product, name='single_product'),
    path('checkout',check ,name='checkout'),

    path('category/', category, name='category'),
    path('category/<str:cat_name>/', category_list, name='category'),
    path('cart', add_to_cart, name='cart'),
    path('add_to_cart/', add_to_cart, name='add_to_cart'),
    path('remove_product/<str:cart_product_name>/',remove_product, name='remove_product'),
    path('change-password/', custom_password_change, name='change_password'),
    path('confirmOrder',confirmations,name='confirmOrder')

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
