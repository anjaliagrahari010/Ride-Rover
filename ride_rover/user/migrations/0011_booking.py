# Generated by Django 5.0.6 on 2025-01-16 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0010_inquiry'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booking_type', models.CharField(choices=[('daily', 'Daily'), ('weekly', 'Weekly'), ('monthly', 'Monthly')], max_length=10)),
                ('pickup_date', models.DateField()),
                ('pickup_time', models.TimeField()),
                ('dropoff_date', models.DateField()),
                ('dropoff_time', models.TimeField()),
            ],
        ),
    ]
