# Generated by Django 3.0 on 2020-01-05 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('motd', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='motd',
            name='text',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
    ]
