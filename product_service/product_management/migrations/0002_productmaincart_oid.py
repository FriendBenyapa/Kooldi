# Generated by Django 5.0.4 on 2024-04-29 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_management', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='productmaincart',
            name='oid',
            field=models.IntegerField(null=True),
        ),
    ]
