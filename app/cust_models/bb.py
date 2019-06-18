from django.db import models
from rest_framework import serializers


class Bb(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    # col1 = models.CharField(max_length=100)

    class Meta:
            db_table = "bb"
            verbose_name = "bb"

class BbSerializer(serializers.ModelSerializer):
    pass

    class Meta:
        model = Bb