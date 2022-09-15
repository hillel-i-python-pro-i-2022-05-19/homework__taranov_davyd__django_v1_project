# Generated by Django 4.1 on 2022-09-15 01:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="RequestLog",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("user", models.CharField(max_length=200, verbose_name="User")),
                ("request_path", models.CharField(max_length=200, verbose_name="Request Path")),
                ("request_count", models.PositiveIntegerField(default=1, verbose_name="Number of requests")),
                (
                    "last_visit",
                    models.DateTimeField(
                        blank=True,
                        default=datetime.datetime(2022, 9, 15, 1, 24, 27, 475043, tzinfo=datetime.timezone.utc),
                        null=True,
                        verbose_name="Last Visit",
                    ),
                ),
            ],
        ),
    ]