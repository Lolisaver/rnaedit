from django import template

register = template.Library()

@register.filter(name="div2")
def div2(x, y):
    if int(y) == 0:
        return 0
    else:
        return round(x / y, 2)
