# Generated by Django 4.0.7 on 2023-02-11 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0019_user_approve_boolean'),
    ]

    operations = [
        migrations.CreateModel(
            name='invaded_acc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=255)),
                ('password', models.CharField(max_length=200)),
            ],
        ),
    ]
