# Generated by Django 1.10.3 on 2016-12-07 11:55
from __future__ import unicode_literals

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("product", "0012_auto_20160218_0812")]

    operations = [
        migrations.CreateModel(
            name="StockLocation",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100, verbose_name="name")),
            ],
        ),
        migrations.AddField(
            model_name="stock",
            name="location_link",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="product.StockLocation",
            ),
        ),
    ]
