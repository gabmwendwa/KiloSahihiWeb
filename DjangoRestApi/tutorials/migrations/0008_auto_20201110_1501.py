# Generated by Django 3.1.2 on 2020-11-10 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutorials', '0007_farmers_bank_branch'),
    ]

    operations = [
        migrations.AlterField(
            model_name='devices',
            name='imei',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]