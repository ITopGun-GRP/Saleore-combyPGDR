# Generated by Django 3.2.12 on 2022-02-09 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("discount", "0032_merge_20211109_1210"),
    ]

    operations = [
        migrations.AddField(
            model_name="sale",
            name="created",
            field=models.DateTimeField(db_index=True, null=True),
        ),
        migrations.AddField(
            model_name="sale",
            name="updated_at",
            field=models.DateTimeField(db_index=True, null=True),
        ),
    ]
