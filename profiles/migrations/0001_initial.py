# Generated by Django 3.0.5 on 2020-07-26 06:46

import datetime
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='SellerProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(blank=True, max_length=20, null=True)),
                ('image', models.FileField(blank=True, null=True, upload_to='F:\\django\\Projects\\ecomm\\ecomm\\media_cdn/Profiles/SellerProfiles', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png'])])),
                ('is_phone_number_verified', models.BooleanField(default=False, null=True)),
                ('is_email_verified', models.BooleanField(default=False, null=True)),
                ('is_seller_verified', models.BooleanField(default=True, null=True)),
                ('account_created_date', models.DateTimeField(default=datetime.datetime(2020, 7, 26, 12, 16, 18, 411997), null=True)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CustomerProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(blank=True, max_length=20, null=True)),
                ('image', models.FileField(blank=True, null=True, upload_to='F:\\django\\Projects\\ecomm\\ecomm\\media_cdn/Profiles/CustomerProfiles', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png'])])),
                ('is_phone_number_verified', models.BooleanField(default=False, null=True)),
                ('is_email_verified', models.BooleanField(default=False, null=True)),
                ('is_customer_verified', models.BooleanField(default=True, null=True)),
                ('account_created_date', models.DateTimeField(default=datetime.datetime(2020, 7, 26, 12, 16, 18, 411997), null=True)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
