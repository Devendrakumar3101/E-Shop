from django import template

register = template.Library()

@register.filter()
def get_multiply(var1, var2):

    return var1 * var2