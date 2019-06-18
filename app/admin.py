from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import SysUser

# Register your models here.
admin.site.register(SysUser, UserAdmin)