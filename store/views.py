from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password, check_password
from .models.product import Product
from .models.category import Category
from .models.customer import Customer
from .models.checkout import Checkout

# Create your views here.
def index(request):
    # return HttpResponse("<h1>this is home page</h1>")

    if request.method == 'GET':

        # request.session.flush()
        products = None
        categories = Category.get_all_category()

        # print(request.GET)

        categoryID = request.GET.get('category_id')

        if categoryID:
            products = Product.get_all_products_by_category_id(categoryID)
        else:
            products = Product.get_all_products()
        
        return render(request, 'index.html', {'products':products, 'categories':categories})
        # return render(request, 'orders/order.html')

    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        remove_item = request.POST.get('remove_item')
        # print(remove_item)
        # print(product_id)

        cart = request.session.get('cart')

        if cart:
            quantity = cart.get(product_id)
            if quantity:
                if remove_item:
                    if quantity == 1:
                        cart.pop(product_id)
                    else:
                        cart[product_id] = quantity-1
                else:
                    cart[product_id] = quantity+1
            else:
                cart[product_id] = 1
        else:
            cart = {}
            cart[product_id] = 1
            
        request.session['cart'] = cart

        # print(request.session['cart'])

        return redirect('homepage')


def signUp(request):
    # return HttpResponse("<h1>This is signup Page</h1>")

    error_msg = None

    # print(request.method)
    if request.method == 'GET':
        # print("this is get request")
        return render(request, 'signup.html')
    else:
        # print("this is post request")
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        all_values = {
            'first_name':first_name,
            'last_name':last_name,
            'email':email,
            'phone':phone,
            'username':username,
        }

        isEmailExists = Customer.objects.filter(email=email)
        isUsernameExists = Customer.objects.filter(username=username)
        # print(isEmailExists)
        # print(isUsernameExists)

        if not first_name:
            error_msg = "First name is required!!"
        elif len(first_name) < 3:
            error_msg = "First name should be three character long or more!!"
        elif not email:
            error_msg = "Email is required"
        elif isEmailExists:
            error_msg = "Email id is already registered"
        elif not phone:
            error_msg = "Phone is required"
        elif len(phone) >15 or len(phone)<10 :
            error_msg = "Please enter valid phone no."
        elif not username:
            error_msg = "Username is required"
        elif len(username) <6:
            error_msg = "Username must be 6 character long"
        elif isUsernameExists:
            error_msg = "Username is already exists in our database. Please select different username."
        elif not password1:
            error_msg = "Paasword is required"
        elif len(password1) <8:
            error_msg = "Password must be 8 character long"
        elif password1 != password2:
            error_msg = "Both password are not same"
        
        if not error_msg:
            hasher_password = make_password(password1)
            # print(hasher_password)
            register_customer = Customer.objects.create(firstname=first_name, lastname=last_name, email=email, phone=phone, username=username, password=hasher_password)

            # print(first_name,last_name,email, phone,username, password1, password2)
            # return HttpResponse("regitered successfully...")
            return redirect('login')
        else:

            params = {
                'error_msg':error_msg,
                'all_values':all_values,
            }

            return render(request, 'signup.html', params)


def loginPage(request):
    # return HttpResponse("<h1>This is loginPage</h1>")

    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')

        print(username, password)

        try:
            customer = Customer.objects.get(username=username)
            if customer:
                password_checking = check_password(password, customer.password)
                if password_checking:
                    request.session['customer'] = customer.id
                    # print(password_checking)
                    return redirect('/')
                else:
                    error_msg = "username or password is wrong!!"
                    return redirect('login')
            else:
                error_msg = "username or password is wrong!!"
                return redirect('/login/')
        except:
            error_msg = "username or password is wrong!!"
            return render(request, 'login.html', {'error_msg':error_msg})

        
def logoutPage(request):
    request.session.clear()
    return redirect('login')


def cartPage(request):
    cart = request.session.get('cart')
    # print(cart)
    if cart is None:
        request.session['cart'] = {}
        ids_list = []

        Products = Product.get_product_by_id(ids_list)
    else:
        ids_list = list(cart.keys())

        Products = Product.get_product_by_id(ids_list)

    print(Products)

    params = {
        'Products' : Products,
    }
    return render(request, 'cart.html', params)

def removeCartProduct(request, product_id):
    # print(request.session.get('cart'))
    my_cart = request.session.get('cart')
    print(my_cart)
    my_cart.pop(product_id)

    request.session['cart'] = my_cart # to update cart

    return redirect('cart')

def CheckoutPage(request):
    if request.method == 'POST':
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        customer = request.session.get('customer')
        cart = request.session.get('cart')
        products = Product.get_product_by_id(list(cart.keys()))

        print(address, phone, customer, cart, products)
        
        for product in products:
            order = Checkout.objects.create(customer = Customer(id=customer),
                                            product = product,
                                            quantity = cart.get(str(product.id)),
                                            price = product.price,
                                            address = address,
                                            phone = phone)
        request.session['cart'] = {}

    return redirect('order')

def OrderPage(request):
    if request.method == 'GET':
        # print(request.session.get('customer'))
        customer_id = request.session.get('customer')

        all_order = Checkout.objects.filter(customer = customer_id).order_by('-date')
        # print(all_order)

        params = {
            'all_order': all_order,
        }
        return render(request, 'order.html', params)

