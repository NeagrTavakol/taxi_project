# Generated by Django 3.1.14 on 2022-11-05 10:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='req_taxi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orig_addr', models.CharField(max_length=1000)),
                ('dest_addr', models.CharField(max_length=1000)),
                ('search_for_taxi', models.BooleanField(default=True)),
                ('achieve_dest', models.BooleanField(default=False)),
                ('travel_costs', models.IntegerField()),
                ('type_travel', models.CharField(choices=[('Delivery', 'delivery'), ('Taxi', 'taxi'), ('Truck', 'truck'), ('Pickup_truck', 'pickup_truck')], default='Taxi', max_length=15)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]