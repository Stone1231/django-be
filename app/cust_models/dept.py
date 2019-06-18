from django.db import models
from rest_framework import serializers


class Dept(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=100)

    class Meta:
        db_table = "dept"
        verbose_name = "dept"

class DeptSerializer(serializers.ModelSerializer):
    pass

    class Meta:
        model = Dept
        fields = "__all__"