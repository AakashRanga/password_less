# Generated by Django 4.0.7 on 2023-02-14 04:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0021_users_details_secure'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users_details',
            name='secure',
            field=models.BooleanField(default=True),
        ),
    ]