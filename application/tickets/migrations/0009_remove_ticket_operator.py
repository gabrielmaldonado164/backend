# Generated by Django 3.2.6 on 2021-09-28 03:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0008_alter_ticket_operator'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='operator',
        ),
    ]