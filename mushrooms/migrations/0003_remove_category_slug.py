# Generated by Django 4.1.3 on 2022-11-26 19:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("mushrooms", "0002_category_slug"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="category",
            name="slug",
        ),
    ]
