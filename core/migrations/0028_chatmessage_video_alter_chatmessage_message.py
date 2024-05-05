# Generated by Django 5.0.2 on 2024-02-24 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0027_alter_fooditem_image_chatmessage'),
    ]

    operations = [
        migrations.AddField(
            model_name='chatmessage',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to='videos/'),
        ),
        migrations.AlterField(
            model_name='chatmessage',
            name='message',
            field=models.TextField(blank=True, null=True),
        ),
    ]
