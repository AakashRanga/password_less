# Generated by Django 4.0.7 on 2022-12-16 23:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_purchase'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='image',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]