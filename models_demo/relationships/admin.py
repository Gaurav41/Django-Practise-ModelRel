from django.contrib import admin
from . models import AppUser,UserDetails
# Register your models here.

# admin.site.register(Employee)


@admin.register(AppUser)
class AppUserAdmin(admin.ModelAdmin):
    list_display = ['user_name','password','is_staff']

@admin.register(UserDetails)
class UserDetailsAdmin(admin.ModelAdmin):
    list_display = ['appuser','mobile_no','aadhaar_no','updated_on']

# @admin.register(ABC)
# class PageAdmin(admin.ModelAdmin):
#     list_display = ['likes',]

