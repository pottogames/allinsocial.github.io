# Generated by Django 5.0.2 on 2024-02-24 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0033_group_members_alter_group_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='group_images/'),
        ),
    ]
