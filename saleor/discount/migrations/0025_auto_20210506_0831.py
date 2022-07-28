# Generated by Django 3.1.8 on 2021-05-06 08:31

import django.contrib.postgres.indexes
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("discount", "0024_orderdiscount"),
    ]

    operations = [
        migrations.AddIndex(
            model_name="orderdiscount",
            index=django.contrib.postgres.indexes.GinIndex(
                fields=["name", "translated_name"], name="discount_or_name_d16858_gin"
            ),
        ),
    ]
