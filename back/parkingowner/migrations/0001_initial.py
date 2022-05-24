# Generated by Django 3.2.9 on 2021-12-21 23:34

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Parking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isPrivate', models.BooleanField(default=False)),
                ('parkingName', models.CharField(max_length=200)),
                ('location', models.CharField(max_length=100)),
                ('parkingPhoneNumber', models.CharField(max_length=30)),
                ('capacity', models.IntegerField(default=0)),
                ('parkingPicture', models.ImageField(blank=True, upload_to='parkingpictures/')),
                ('rating', models.FloatField(default=0)),
                ('validationStatus', models.CharField(choices=[('V', 'Valid'), ('I', 'Invalid'), ('P', 'Pending')], default='I', max_length=1)),
                ('pricePerHour', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Validation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nationalCode', models.CharField(max_length=10)),
                ('validationFiles', models.FileField(upload_to='validationfiles/')),
                ('postalCode', models.CharField(max_length=10)),
                ('validationCode', models.IntegerField()),
                ('time_Added', models.DateTimeField(default=django.utils.timezone.now)),
                ('parking', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='parkingowner.parking')),
            ],
        ),
        migrations.CreateModel(
            name='Template',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('openAt', models.DateTimeField()),
                ('closeAt', models.DateTimeField()),
                ('weekDay', models.IntegerField(default=0)),
                ('parking', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parkingowner.parking')),
            ],
        ),
        migrations.CreateModel(
            name='Period',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('capacity', models.IntegerField(default=0)),
                ('duration', models.DurationField(default=datetime.timedelta(seconds=1800))),
                ('startTime', models.DateTimeField()),
                ('endTime', models.DateTimeField()),
                ('weekDay', models.IntegerField(default=0)),
                ('is_active', models.BooleanField(default=True)),
                ('parking', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parkingowner.parking')),
            ],
        ),
        migrations.CreateModel(
            name='ParkingOwner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='parking',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='parkingowner.parkingowner'),
        ),
    ]
