# Generated by Django 4.0.5 on 2023-04-04 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bn', '0005_mohammedusers_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='balance',
            name='balance',
        ),
        migrations.RemoveField(
            model_name='balance',
            name='username',
        ),
        migrations.AddField(
            model_name='balance',
            name='entry_price',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='balance',
            name='leverage',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='balance',
            name='side',
            field=models.CharField(default='empty', max_length=232323),
        ),
        migrations.AddField(
            model_name='balance',
            name='stop_loss',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='balance',
            name='symbol',
            field=models.CharField(default='empty', max_length=232323),
        ),
        migrations.AddField(
            model_name='balance',
            name='tp1',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='balance',
            name='tp2',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='balance',
            name='tp3',
            field=models.FloatField(default=0),
        ),
    ]
