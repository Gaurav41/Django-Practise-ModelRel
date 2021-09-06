from django.contrib import admin
from . models import AppUser,UserDetails,Temp,Post,Product
# Register your models here.

# admin.site.register(Employee)


@admin.register(AppUser)
class AppUserAdmin(admin.ModelAdmin):
    list_display = ['user_name','password','is_staff']

@admin.register(UserDetails)
class UserDetailsAdmin(admin.ModelAdmin):
    list_display = ['appuser','mobile_no','aadhaar_no','updated_on']

@admin.register(Temp)
class PageAdmin(admin.ModelAdmin):
    list_display = ['appuser','mobile_no','aadhaar_no','updated_on','likes']

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['user','post_title','post_des','post_publish_date']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['prod_name','prod_price','ordered_by']
