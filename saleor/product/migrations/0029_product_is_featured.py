# Generated by Django 1.10.5 on 2017-01-30 10:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("product", "0028_merge_20170116_1016")]

    operations = [
        migrations.AddField(
            model_name="product",
            name="is_featured",
            field=models.BooleanField(default=False, verbose_name="is featured"),
        )
    ]
