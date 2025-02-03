from django import template

register = template.Library()

@register.filter
def get_attr(obj, attr_name):
    """ Récupère un attribut d'un objet dans un template Django """
    return getattr(obj, attr_name, "")
