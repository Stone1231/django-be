from django.db import models
from rest_framework import serializers


class Proj(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=100)

    class Meta:
            db_table = "proj"
            verbose_name = "proj"

class ProjSerializer(serializers.ModelSerializer):
    pass

    class Meta:
        model = Proj
        fields = "__all__"