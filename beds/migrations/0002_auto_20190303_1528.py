# Generated by Django 2.0.5 on 2019-03-03 21:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('events', '0001_initial'),
        ('beds', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bedavailability',
            name='event_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.Event'),
        ),
        migrations.AddField(
            model_name='bedavailability',
            name='org_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.Organization'),
        ),
    ]
