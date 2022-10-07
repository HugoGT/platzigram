"""Posts admin classes"""


from django.contrib import admin

from .models import Post


class PostAdmin(admin.ModelAdmin):
    """Posts Admin model"""

    list_display = ('user', 'title', 'photo',)
    list_display_links = ('user',)
    list_filter = (
                'created',
                'modified'
    )

admin.site.register(Post, PostAdmin)
