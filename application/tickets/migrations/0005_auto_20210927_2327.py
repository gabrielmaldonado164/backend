# Generated by Django 3.2.6 on 2021-09-28 02:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0004_alter_comment_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='text',
            field=models.TextField(blank=True, max_length=255, verbose_name='Comentario'),
        ),
        migrations.AlterField(
            model_name='history',
            name='text',
            field=models.TextField(blank=True, verbose_name='Historia'),
        ),
    ]
