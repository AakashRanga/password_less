# Generated by Django 4.0.7 on 2023-02-03 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0014_remove_user_approve_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_approve',
            name='status',
            field=models.CharField(default=None, max_length=255),
        ),
    ]
