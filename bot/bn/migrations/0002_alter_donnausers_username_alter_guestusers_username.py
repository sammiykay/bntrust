# Generated by Django 4.0.5 on 2022-06-13 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bn', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donnausers',
            name='username',
            field=models.CharField(max_length=100000000),
        ),
        migrations.AlterField(
            model_name='guestusers',
            name='username',
            field=models.CharField(max_length=10000000000),
        ),
    ]
