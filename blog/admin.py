from django.contrib import admin

from blog.models import Blog


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'body', 'image', 'count_views', 'date_publications', 'is_publication')
    list_filter = ('is_publication',)
    search_fields = ('title', 'date_publications',)