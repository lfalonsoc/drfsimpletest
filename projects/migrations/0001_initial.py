# Generated by Django 4.2.4 on 2023-08-25 01:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Project",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=200)),
                ("description", models.TextField()),
                ("technology", models.CharField(max_length=200)),
                ("create_at", models.DateTimeField(auto_now_add=True)),
                ("modify_at", models.DateField(auto_now=True)),
            ],
        ),
    ]