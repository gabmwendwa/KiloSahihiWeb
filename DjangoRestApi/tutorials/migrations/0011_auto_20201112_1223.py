# Generated by Django 3.1.2 on 2020-11-12 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutorials', '0010_auto_20201112_1154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='factories',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]