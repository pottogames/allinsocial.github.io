# Generated by Django 5.0.2 on 2024-03-02 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0040_messages'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='share_count',
            field=models.IntegerField(default=0),
        ),
    ]
