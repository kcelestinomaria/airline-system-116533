# Generated by Django 5.1.3 on 2024-12-22 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0002_flight_base_price_flight_seat_classes_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flight',
            name='base_price',
            field=models.DecimalField(decimal_places=2, default=100.0, max_digits=10),
        ),
    ]
