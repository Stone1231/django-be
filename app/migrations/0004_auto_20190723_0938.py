# Generated by Django 2.2.2 on 2019-07-23 01:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20190722_1604'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='photo',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]