from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from account.models import Account


class AccountAdmin(UserAdmin):
    list_display = ('email', 'username', 'date_joined', 'last_login', 'is_admin', 'is_staff')
    search_fields = ('email', 'username')
    list_filter = ('is_admin', 'is_staff', 'is_active', 'date_joined', 'last_login',)
    readonly_fields = ('date_joined', 'last_login')

    filter_horizontal = ()
    fieldsets = ()

admin.site.register(Account, AccountAdmin)