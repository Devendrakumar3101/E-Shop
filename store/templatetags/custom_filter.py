from django import template
from store.models.customer import Customer

register = template.Library()

@register.filter()
def get_multiply(var1, var2):

    return var1 * var2

@register.filter()
def get_logged_customer(customer_id):

    customer_name = Customer.objects.get(id = customer_id).firstname
    # print(customer_name)

    return customer_name