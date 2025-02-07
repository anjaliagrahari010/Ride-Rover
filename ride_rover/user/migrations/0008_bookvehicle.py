# Generated by Django 5.0.6 on 2025-01-13 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_alter_vehicle_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookVehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price_per_day', models.DecimalField(decimal_places=2, max_digits=10)),
                ('price_per_week', models.DecimalField(decimal_places=2, max_digits=10)),
                ('price_per_month', models.DecimalField(decimal_places=2, max_digits=10)),
                ('image', models.FileField(upload_to='')),
            ],
        ),
    ]
