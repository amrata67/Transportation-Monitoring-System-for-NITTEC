# Generated by Django 3.0.4 on 2020-04-09 00:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('incident', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='incidentlog',
            name='id',
            field=models.AutoField(db_column='ID', primary_key=True, serialize=False),
        ),
    ]
