# Generated by Django 5.0.6 on 2024-06-25 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("data", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="variable",
            name="name",
            field=models.CharField(db_index=True, max_length=50, unique=True),
        ),
    ]
