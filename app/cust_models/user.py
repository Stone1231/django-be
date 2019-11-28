from django.db import models
from rest_framework import serializers
from .dept import Dept
from .proj import Proj


class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45)
    hight = models.IntegerField(default=0)
    birthday = models.DateField()
    photo = models.CharField(max_length=100, null=True, blank=True)
    dept = models.ForeignKey(
        Dept,
        on_delete=models.CASCADE,
        related_name='users')
    projs = models.ManyToManyField(
        Proj,
        through='UserProjMapping',
        related_name="users")

    class Meta:
        db_table = "user"
        verbose_name = "user"


class UserProjMapping(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='maps')
    proj = models.ForeignKey(
        Proj,
        on_delete=models.CASCADE,
        related_name='maps')

    class Meta:
        db_table = "user_proj"
        verbose_name = "user proj mapping"


class UserSerializer(serializers.ModelSerializer):
    dept = serializers.PrimaryKeyRelatedField(
        read_only=False,
        many=False,
        queryset=Dept.objects.all())
    projs = serializers.PrimaryKeyRelatedField(
        read_only=False,
        many=True,
        queryset=Proj.objects.all())
    # dept = serializers.PrimaryKeyRelatedField(
    #     read_only=True,
    #     many=False)
    # projs = serializers.PrimaryKeyRelatedField(
    #     read_only=True,
    #     many=True)

    class Meta:
        model = User
        fields = "__all__"


class UserWriteSerializer(serializers.ModelSerializer):
    # projs = serializers.PrimaryKeyRelatedField(
    #     many=True,
    #     read_only=False,
    #     queryset=Proj.objects.all())

    class Meta:
        model = User
        fields = "__all__"


class UserSimpleSerializer(serializers.ModelSerializer):
    pass

    class Meta:
        model = User
        exclude = ("hight",)
        # exclude = ("hight", "photo",)
