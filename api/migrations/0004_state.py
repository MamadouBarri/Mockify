# Generated by Django 3.1.2 on 2020-10-17 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_city_countrycode_countryname_currency_email_firstname_lastname_phone_streetaddress_zip'),
    ]

    operations = [
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.CharField(max_length=10)),
            ],
        ),
    ]
