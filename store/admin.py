from django.contrib import admin
from .models.product import Product
from .models.category import Category
from .models.customer import Customer
from .models.checkout import Checkout

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category') #it can be a list or tuple
admin.site.register(Product, ProductAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',) # ensure last with a comma to create a tuple with only one value
admin.site.register(Category, CategoryAdmin)

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('firstname', 'lastname', 'email', 'phone', 'username')
admin.site.register(Customer, CustomerAdmin)

admin.site.register(Checkout)



# modifying admin panel

admin.site.site_title = "EShop"
admin.site.site_header = 'E-Shop'
admin.site.index_title = "Welcome to E-Shop"

