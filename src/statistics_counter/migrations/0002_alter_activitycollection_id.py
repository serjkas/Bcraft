# Generated by Django 3.2.9 on 2021-11-26 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('statistics_counter', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activitycollection',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]