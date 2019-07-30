from django.db import models
from django.contrib.auth.models import AbstractUser
from rest_framework import serializers

# Create your models here.


class SysUser(AbstractUser):
    role = models.CharField(max_length=10)
    pass

    class Meta:
        db_table = "sys_user"
        verbose_name = "sysuser"


class SysUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = SysUser
        fields = '__all__'


class SysUserSimpleSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()

    class Meta:
        model = SysUser
        fields = (
            'username', 
            'first_name', 
            'last_name',
            'email',  
            'full_name',
            'role')

    def get_full_name(self, obj):
        index = obj.email.find('@')
        return obj.email[0: index]

# from .cust_models import *