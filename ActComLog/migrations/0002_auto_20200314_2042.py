# Generated by Django 2.2.5 on 2020-03-14 20:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ActComLog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='acl',
            old_name='ddm',
            new_name='dates_to_remember',
        ),
        migrations.RenameField(
            model_name='acl',
            old_name='dtr',
            new_name='day_to_day_message',
        ),
        migrations.RenameField(
            model_name='acl',
            old_name='ltm',
            new_name='long_term_message',
        ),
    ]