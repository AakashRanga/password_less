# Generated by Django 4.0.7 on 2023-01-25 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_rename_username_loginattempt_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='loginattempt',
            name='is_correct',
        ),
        migrations.AddField(
            model_name='loginattempt',
            name='login_attempts',
            field=models.IntegerField(default=0),
        ),
    ]