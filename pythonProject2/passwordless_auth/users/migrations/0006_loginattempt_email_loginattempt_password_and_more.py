# Generated by Django 4.0.7 on 2023-01-25 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_remove_loginattempt_created_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='loginattempt',
            name='email',
            field=models.CharField(default='exit', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='loginattempt',
            name='password',
            field=models.CharField(default='exit', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='users_details',
            name='login_attempts',
            field=models.IntegerField(default=0),
        ),
    ]
