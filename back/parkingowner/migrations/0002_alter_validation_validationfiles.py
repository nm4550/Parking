# Generated by Django 3.2.9 on 2021-12-22 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parkingowner', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='validation',
            name='validationFiles',
            field=models.FileField(blank=True, upload_to='validationfiles/'),
        ),
    ]
