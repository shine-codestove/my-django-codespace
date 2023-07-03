# Generated by Django 4.2.3 on 2023-07-03 12:50

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Person",
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
                ("first_name", models.CharField(max_length=30)),
                ("last_name", models.CharField(max_length=30)),
                ("age", models.IntegerField(default=0)),
                (
                    "sex",
                    models.CharField(
                        choices=[("male", "남"), ("female", "여")],
                        default="",
                        max_length=20,
                    ),
                ),
            ],
            options={
                "db_table": "person",
            },
        ),
    ]