# Generated by Django 4.1.2 on 2022-10-27 21:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trip',
            name='car',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='car', to='service.car'),
        ),
        migrations.AlterField(
            model_name='trip',
            name='driver',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='driver', to='service.driver'),
        ),
    ]
