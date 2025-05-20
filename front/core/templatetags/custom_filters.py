from django import template
from core.models import *

register = template.Library()

@register.filter(name='format_phone')
def format_phone(phone_number):
    return f"{phone_number[0]} {phone_number[1:5]} {phone_number[5:]}" if len(phone_number) > 6 else f"{phone_number[:]}"


@register.filter(name='format_rut')
def format_rut(full_rut):
    data = full_rut.split('-')
    if (len(data) == 1):
        dv = full_rut[-1]
        rut = full_rut[0:-1]
    else:
        dv = full_rut.split('-')[1]
        rut = full_rut.split('-')[0]
    #77 589 601-9
    return f"{rut[:-6]}.{rut[-6:-3]}.{rut[-3:]}-{dv}" 

@register.filter(name='usuario')
def usuario(id):
    name = USER_TYPES[int(id)][1]
    return name
