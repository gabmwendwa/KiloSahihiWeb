# Generated by Django 3.1.2 on 2020-11-06 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutorials', '0006_auto_20201030_1508'),
    ]

    operations = [
        migrations.AddField(
            model_name='farmers',
            name='bank_branch',
            field=models.CharField(default=None, max_length=50),
            preserve_default=False,
        ),
    ]
