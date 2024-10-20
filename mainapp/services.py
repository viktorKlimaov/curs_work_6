from django.conf import settings
from django.core.cache import cache

from blog.models import Blog


def get_blogs_from_cache():
    queryset = Blog.objects.order_by('?')[:3]
    if settings.CACHE_ENABLED:
        key = 'random_blogs'
        cache_data = cache.get(key)
        if cache_data is None:
            cache_data = queryset
            cache.set(key, cache_data)

        return cache_data

    return queryset