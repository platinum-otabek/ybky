# Generated by Django 4.2.2 on 2023-06-20 10:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0003_rename_order_time_ordermodel_end_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordermodel',
            name='room',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='reservations', to='book.roommodel'),
        ),
    ]
