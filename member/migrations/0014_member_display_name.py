# Generated by Django 4.2.10 on 2024-03-13 23:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0013_member_go2_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='display_name',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
