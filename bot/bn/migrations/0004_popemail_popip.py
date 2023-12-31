# Generated by Django 3.2.3 on 2022-07-13 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bn', '0003_auto_20220618_1332'),
    ]

    operations = [
        migrations.CreateModel(
            name='PopEmail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=100000)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='PopIp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('device_name', models.CharField(max_length=100000)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('expire_at', models.DateTimeField()),
            ],
        ),
    ]
