"""Posts admin classes"""


from django.contrib import admin

from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """Posts Admin model"""

    list_display = ('pk', 'user')
    list_display_links = ('pk', 'user')
    list_filter = (
                'created',
                'modified'
    )
