# Generated by Django 5.0.3 on 2024-03-16 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0054_campaign1_remove_store_campaign_purchase1_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='campaign1',
            name='image',
            field=models.ImageField(default='default_image.jpg', upload_to='campaign_images/'),
        ),
    ]