# Generated by Django 3.1.4 on 2021-01-08 09:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tutorials', '0004_auto_20201221_1017'),
    ]

    operations = [
        migrations.RenameField(
            model_name='audits',
            old_name='audit',
            new_name='date',
        ),
    ]
