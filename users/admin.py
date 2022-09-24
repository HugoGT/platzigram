"""Users admin classes"""


from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from .models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """Profile admin"""

    list_display = ('pk', 'user', 'phone_number', 'website', 'picture')
    list_display_links = ('pk', 'user')
    list_editable = ('phone_number', 'website', 'picture')

    list_filter = (
        'user__is_staff',
        'user__is_active',
        'created',
        'modified',
        )

    search_fields = (
        'user__username',
        'user__first_name',
        'user__lastname',
        'phone_number',
        'user__email',
        )

    readonly_fields = ('user', 'created', 'modified')

    fieldsets = (
        ('Profile', {
            'fields': (
                ('user', 'picture'),
                ('biography'),
                ('phone_number', 'website'),
            ),
        }),
        ('Metadata', {
            'fields': (
                ('created', 'modified'),
            ),
        }),
    )


class ProfileInLine(admin.StackedInline):
    """Profile in-line admin for users"""

    model = Profile
    can_delete = False
    verbose_name_plural = 'profiles'


class UserAdmin(BaseUserAdmin):
    """Add profile admin to base user admin"""

    inlines = (ProfileInLine,)

    list_display = (
        'username',
        'email',
        'first_name',
        'last_name',
        'is_active',
        'is_staff',
        )


admin.site.unregister(User)
admin.site.register(User, UserAdmin)