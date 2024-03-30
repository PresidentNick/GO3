# Generated by Django 4.2.11 on 2024-03-25 23:46

# a data migration for moving from old, bad date/time handling to perfect, new date/time handling

from django.db import migrations
import pytz
import datetime

def update_dates(apps, schema_editor):

    def _update(g,is_full_day,has_call_time,has_set_time,has_end_time):
        g.is_full_day = is_full_day
        g.has_call_time = has_call_time
        g.has_set_time = has_set_time
        g.has_end_time = has_end_time
        g.save()
        return

    Gig = apps.get_model('gig', 'Gig')
    for g in Gig.objects.all():
        zone = pytz.timezone(g.band.timezone)

        # convert to local times for ease of dealing with midnight
        date = g.date.astimezone(zone)
        setdate = g.setdate.astimezone(zone) if g.setdate else None
        enddate = g.enddate.astimezone(zone) if g.enddate else None

        # this is this a full-day gig?

        # if it has an end date that isn't the date, it is
        if enddate and date.date() != enddate.date():
            _update(g,True,False,False,False)
            continue

        # if it doen't have an end date at all and the "date" time is midnight,
        # it was probably saved without a time so it's full-day
        if enddate is None and setdate is None and date.time() == datetime.time(0,0):
            _update(g,True,False,False,False)
            continue

        # if it has believable times for date, settime, endtime, mark them as such
        _update(g,
                False,
                False if date.time() == datetime.time(0,0) else True,
                False if setdate is None else (False if setdate.time() == datetime.time(0,0) else True),
                False if enddate is None else (False if enddate.time() == datetime.time(0,0) else True)
                )


        g.save()

def unupdate_dates(apps, schema_editor):
    return

class Migration(migrations.Migration):


    dependencies = [
        ('gig', '0019_gig_has_call_time_gig_has_end_time_gig_has_set_time_and_more'),
    ]

    operations = [
        migrations.RunPython(update_dates, unupdate_dates)
    ]
