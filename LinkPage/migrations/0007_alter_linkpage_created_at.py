# Generated by Django 4.2.1 on 2023-09-23 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LinkPage', '0006_link_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='linkpage',
            name='created_at',
            field=models.DateField(auto_now_add=True),
        ),
    ]