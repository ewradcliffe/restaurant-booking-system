# Generated by Django 4.2.14 on 2024-08-13 13:15

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
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reservation_name', models.CharField(max_length=60)),
                ('reservation_email', models.EmailField(blank=True, max_length=254, null=True)),
                ('reservation_date', models.DateField()),
                ('reservation_time', models.CharField(choices=[('12:00', '12:00'), ('12:30', '12:30'), ('13:00', '13:00'), ('13:30', '13:30'), ('18:00', '18:00'), ('18:30', '18:30'), ('19:00', '19:00'), ('19:30', '19:30'), ('20:00', '20:00'), ('20:30', '20:30'), ('21:00', '21:00'), ('21:30', '21:30')], max_length=10)),
                ('number_of_guests', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9')], max_length=10)),
                ('reservation_created_on', models.DateTimeField(auto_now_add=True)),
                ('reservation_updated_on', models.DateTimeField(auto_now=True)),
                ('reservation_booked_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['reservation_date', '-reservation_time'],
            },
        ),
    ]
