# Generated by Django 4.0.7 on 2023-01-25 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_loginattempt_email_loginattempt_password_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='loginattempt',
            name='pattern',
            field=models.CharField(default='exit', max_length=50),
            preserve_default=False,
        ),
    ]
