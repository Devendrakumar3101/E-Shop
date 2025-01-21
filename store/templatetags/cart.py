from django import template

register = template.Library()

@register.filter(name='is_in_cart')
def is_in_cart(product, cart):

    cart_keys = cart.keys()

    for key in cart_keys:
        if int(key) == product.id :
            return True

    print(product, cart)
    return False


@register.filter(name='cart_quantity')
def cart_quantity(product, cart):

    cart_keys = cart.keys()

    for key in cart_keys:
        if int(key) == product.id :
            return cart.get(key)

    return 0


@register.filter(name='get_price')
def get_price(product, cart):
    return product.price * cart_quantity(product, cart)


@register.filter(name='get_total_price')
def get_total_price(Products, cart):
    sum = 0

    for product in Products:
        sum += get_price(product, cart)

    return sum

