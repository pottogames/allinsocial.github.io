# Generated by Django 5.0.2 on 2024-02-17 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_cartitem'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartitem',
            name='added_at',
        ),
        migrations.AlterField(
            model_name='cartitem',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
    ]