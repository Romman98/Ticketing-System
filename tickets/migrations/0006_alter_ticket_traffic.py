# Generated by Django 5.0.7 on 2024-08-15 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0005_sample'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='traffic',
            field=models.CharField(choices=[('incoming', 'Incoming'), ('outgoing', 'Outgoing')], max_length=50),
        ),
    ]