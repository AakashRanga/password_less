# Generated by Django 4.0.7 on 2023-02-11 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0018_alter_user_approve_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_approve',
            name='boolean',
            field=models.BooleanField(default=False),
        ),
    ]
