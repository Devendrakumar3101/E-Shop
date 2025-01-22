from django.contrib import admin
from django.urls import path, include
from store import views
from .middlewares.auth import auth_middleware

urlpatterns = [
    path('', views.index, name='homepage'),
    path('signup/', views.signUp, name='signup'),
    path('login/', views.loginPage, name='login'),
    path('profile/', views.ProfilePage, name='profile'),
    path('logout/', views.logoutPage, name='logout'),
    path('cart/', views.cartPage, name='cart'),
    path('cart/remove/<product_id>/', views.removeCartProduct, name='removeCartProduct'),
    path('checkout/', auth_middleware(views.CheckoutPage), name='checkout'),
    path('order/', auth_middleware(views.OrderPage), name='order'),
]
