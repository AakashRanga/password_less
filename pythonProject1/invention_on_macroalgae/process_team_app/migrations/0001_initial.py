# Generated by Django 4.0.7 on 2022-12-13 22:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Process_team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255)),
                ('password', models.CharField(max_length=200)),
                ('phone', models.BigIntegerField()),
                ('address', models.CharField(max_length=255)),
            ],
        ),
    ]
