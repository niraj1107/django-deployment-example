from django import template

register=template.Library()

@register.filter(name='cut')
def cut(value,arg):
    """
    This cut all value of arg from the string!
    """
    return value.replace(arg,'')
