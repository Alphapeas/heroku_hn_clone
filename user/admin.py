from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username',  'is_active')
    list_display_links = ('username', )
    list_editable = ('is_active',)


admin.site.site_title = _('News (That is not Hacker News clone) Dashboard')
admin.site.site_header = _('News Dashboard')
