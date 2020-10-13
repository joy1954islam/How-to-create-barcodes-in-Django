# Generated by Django 2.2.16 on 2020-10-13 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BarCode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SiteName', models.CharField(max_length=200)),
                ('barcode', models.ImageField(blank=True, upload_to='images/')),
                ('country_id', models.CharField(max_length=1, null=True)),
                ('manufacturer_id', models.CharField(max_length=6, null=True)),
                ('SiteName_id', models.CharField(max_length=5, null=True)),
            ],
        ),
    ]
