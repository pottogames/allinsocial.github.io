# Generated by Django 5.0.2 on 2024-02-20 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0018_remove_userprofile_paypal_email_transaction'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='sku',
            field=models.CharField(default='DEFAULT_SKU', max_length=50),
        ),
    ]
