# Generated by Django 5.0.2 on 2024-04-20 19:32

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('image_url', models.URLField()),
                ('car_status', models.CharField(max_length=20)),
                ('mileage', models.IntegerField()),
                ('year', models.PositiveIntegerField()),
                ('description', models.TextField(default='')),
                ('engine_type', models.CharField(default='', max_length=100)),
                ('transmission_type', models.CharField(default='', max_length=50)),
                ('fuel_type', models.CharField(default='', max_length=30)),
                ('cooling_system', models.CharField(default='', max_length=50)),
                ('engine_condition', models.CharField(default='', max_length=10)),
                ('transmission_condition', models.CharField(default='', max_length=10)),
                ('suspension_condition', models.CharField(default='', max_length=10)),
                ('custom_duty', models.CharField(default='', max_length=10)),
                ('kms_classification', models.CharField(default='', editable=False, max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('products', models.ManyToManyField(to='store.product')),
            ],
        ),
    ]