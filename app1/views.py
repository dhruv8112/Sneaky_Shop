from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import authenticate, login

from .models import contact as ContactModel
from .models import *

# Create your views here.


def index(request):
    data = products.objects.all()
    print(data)
    return render(request, 'index.html', {'data': data})


def register_page(request):
    if request.method == 'POST':
        uname = request.POST.get('name')
        uemail = request.POST.get('email')
        upass = request.POST.get('password')
        ucon_password = request.POST.get('confirm_password')
        uaddress = request.POST.get('address')

        # Check if the user with the same username already exists
        if User.objects.filter(username=uname).exists():
            # User with the same username already exists
            # Handle the appropriate logic (e.g., display an error message)
            return HttpResponse('Username already exists')

        # Create a new user
        my_user = User.objects.create_user(uname, uemail, upass)
        my_user.save()
        # Redirect to the login page after successful registration
        return redirect(login)

    # Render the registration form
    return render(request, 'register.html')


def login(request):
    if request.method == "POST":
        email = request.POST.get('user_name')
        password = request.POST.get('user_password')
        print(email, password)
        user = authenticate(request, username=email, password=password)
        if user is not None:
            return redirect('index')
        # Replace 'index' with the appropriate URL name for your index page
        else:
            message = 'Invalid email or password'
            print(message)
            return render(request, 'login.html', {'message': message})
    return render(request, 'login.html')


def contact_us(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        contact_info = request.POST.get('contact')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        print(name, email, contact_info, subject, message)
        cont = ContactModel.objects.create(
            name=name,
            Email=email,
            contact_no=contact_info,
            subject=subject,
            message=message
        )
        cont.save()  # Saving is not necessary when using create()
        return HttpResponse("Your records has been saved successfully")
    return render(request, 'contact.html')


def single_product(request, pro_id):
    show_product = products.objects.filter(pro_id=pro_id).first()
    if request.method == "POST":
        model = Cart()
        model.product_id = request.POST['id']
        model.quantity = request.POST['quantity']
        product_data = products.objects.get(pro_id=request.POST['id'])
        model.total_price = int(product_data.price) * \
            int(request.POST['quantity'])
        model.cart_product_name = products.pro_name
        # model.cart_product_name = show_product.pro_name.value_from_object(show_product)
        model.save()
        return redirect('cart')

    return render(request, 'single-product.html', {'product': show_product})


def category(request):
    category_display = categories.objects.all()
    # category = categories.objects.get(name=cat_name)
    # products_get = products.objects.filter(category=category)

    # context = {
    #     'category': category,
    #     'products': products_get
    # }

    # return render(request, 'category.html', context)

    return render(request, 'category.html', {'category': category_display})


def add_to_cart(request):
    cart_object_get = Cart.objects.all()
    return render(request, 'cart.html', {'cart': cart_object_get})


def custom_password_change(request):
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            user = form.save()
            # Update the session to prevent the user from being logged out
            update_session_auth_hash(request, user)
            messages.success(
                request, 'Your password has been changed successfully.')
            return redirect(reverse('login'))
    else:
        form = PasswordChangeForm(user=request.user)

    return render(request, 'change.html', {'form': form})
