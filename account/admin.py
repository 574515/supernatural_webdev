from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from account.models import Account


class AccountAdmin(UserAdmin):
	list_display = ('email', 'last_login', 'is_active', 'is_admin', 'is_staff', 'is_superuser')
	search_fields = ('email', 'username')
	list_filter = ('is_active', 'is_admin', 'is_staff', 'is_superuser', 'date_joined', 'last_login')
	readonly_fields = ('first_name', 'last_name', 'username', 'email', 'date_joined', 'last_login')

	filter_horizontal = ()
	fieldsets = ()


admin.site.register(Account, AccountAdmin)
