from django import template
from pages.models import Page

#vamos a crear una variable register
register = template.Library()

@register.simple_tag
def get_page_list():
    pages = Page.objects.all()
    return pages