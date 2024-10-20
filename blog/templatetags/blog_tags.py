from django import template

register = template.Library()

# Создание фильтра
@register.filter()
def blog_media(path):
    if path:
        return f'/media/{path}'
    return '#'
