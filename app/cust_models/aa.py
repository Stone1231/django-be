from django.db import models
from rest_framework import serializers


class Aa(models.Model):
    id = models.AutoField(primary_key=True)
    name_en = models.CharField(max_length=100)
    # col1 = models.CharField(max_length=100)

    class Meta:
            db_table = "aa"
            verbose_name = "aa"

class AaSerializer(serializers.ModelSerializer):
    pass

    class Meta:
        model = Aa