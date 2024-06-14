# Generated by Django 4.2.11 on 2024-06-14 00:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0018_alter_memberpreferences_agenda_show_time_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='memberpreferences',
            name='agenda_layout',
            field=models.IntegerField(choices=[(0, 'Need Response'), (1, 'By Band'), (2, 'Single List')], default=0),
        ),
        migrations.AlterField(
            model_name='emailconfirmation',
            name='language',
            field=models.CharField(choices=[('de', 'German'), ('en-US', 'English (US)'), ('en-GB', 'English (UK, AU, NZ, ...)'), ('es', 'Spanish'), ('fr', 'French'), ('it', 'Italian')], default='en-US', max_length=200),
        ),
        migrations.AlterField(
            model_name='invite',
            name='language',
            field=models.CharField(choices=[('de', 'German'), ('en-US', 'English (US)'), ('en-GB', 'English (UK, AU, NZ, ...)'), ('es', 'Spanish'), ('fr', 'French'), ('it', 'Italian')], default='en-US', max_length=200),
        ),
        migrations.AlterField(
            model_name='memberpreferences',
            name='language',
            field=models.CharField(choices=[('de', 'German'), ('en-US', 'English (US)'), ('en-GB', 'English (UK, AU, NZ, ...)'), ('es', 'Spanish'), ('fr', 'French'), ('it', 'Italian')], default='en-US', max_length=200, verbose_name='Language'),
        ),
    ]
