# Generated by Django 4.2.10 on 2024-03-18 02:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0015_auto_20240313_1930'),
    ]

    operations = [
        migrations.AlterField(
            model_name='memberpreferences',
            name='calendar_show_only_committed',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='memberpreferences',
            name='calendar_show_only_confirmed',
            field=models.BooleanField(default=False),
        ),
    ]
