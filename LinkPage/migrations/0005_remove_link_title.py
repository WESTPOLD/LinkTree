# Generated by Django 4.2.1 on 2023-09-23 20:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('LinkPage', '0004_linkpage_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='link',
            name='title',
        ),
    ]
