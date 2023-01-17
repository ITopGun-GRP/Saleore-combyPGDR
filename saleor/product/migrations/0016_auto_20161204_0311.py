# Generated by Django 1.10.3 on 2016-12-04 09:11
from __future__ import unicode_literals

import django.contrib.postgres.fields.hstore
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [("product", "0015_productvariant_attributes")]

    operations = [
        migrations.AlterField(
            model_name="productvariant",
            name="attributes",
            field=django.contrib.postgres.fields.hstore.HStoreField(
                default={}, verbose_name="attributes"
            ),
        )
    ]
