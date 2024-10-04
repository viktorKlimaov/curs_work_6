from django import template

register = template.Library()

# Создание фильтра
@register.filter()
def my_media(path):
    if path:
        return f'/media/{path}'
    return '#'