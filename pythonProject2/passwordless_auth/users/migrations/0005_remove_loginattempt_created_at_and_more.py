# Generated by Django 4.0.7 on 2023-01-25 05:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_remove_loginattempt_is_correct_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='loginattempt',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='loginattempt',
            name='email',
        ),
        migrations.RemoveField(
            model_name='loginattempt',
            name='password',
        ),
    ]
