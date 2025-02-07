# Generated by Django 5.0.6 on 2025-02-02 16:49

import django.db.models.deletion
import user.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0017_remove_booking_booking_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='booking_id',
            field=models.CharField(default=user.models.generate_booking_id, editable=False, max_length=20, unique=True),
        ),
        migrations.AddField(
            model_name='booking',
            name='vehicle',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='user.vehicle'),
        ),
    ]
