# Generated by Django 4.2.2 on 2023-06-20 08:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_ordermodel'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ordermodel',
            old_name='order_time',
            new_name='end_time',
        ),
    ]
