from django.contrib import admin

from blog.models import Blog


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'publication_attribute', 'views_count', 'created_at', 'updated_at',)
    search_fields = ('title', 'content', 'publication_attribute',)
    list_filter = ('created_at',)
    ordering = ('-created_at',)
