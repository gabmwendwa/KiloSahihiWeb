# Generated by Django 3.1.2 on 2020-11-12 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutorials', '0011_auto_20201112_1223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produce',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
