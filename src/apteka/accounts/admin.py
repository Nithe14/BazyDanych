from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


from .forms import UserAdminCreationForm, UserAdminChangeForm
from .models import User


#User = get_user_model()

class UserAdmin(BaseUserAdmin):

    form = UserAdminChangeForm
    add_form = UserAdminCreationForm

    list_display = ('email', 'admin', 'name', 'surname')
    list_filter = ('admin', 'staff', 'active',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('name', 'surname', 'phone_number', 'street', 'flat_number', 'post_code', 'city')}),
        ('Permissions', {'fields': ('admin', 'staff', 'active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'name', 'surname', 'phone_number', 'street', 'flat_number', 'post_code', 'city', 'password1', 'password2')}
         ),
    )
    search_fields = ('email', 'name', 'surname')
    ordering = ('email','name', 'surname')
    filter_horizontal = ()

admin.site.register(User, UserAdmin)

admin.site.unregister(Group)
