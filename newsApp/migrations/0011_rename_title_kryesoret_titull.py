# Generated by Django 4.1 on 2022-09-14 15:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsApp', '0010_alter_kryesoret_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='kryesoret',
            old_name='title',
            new_name='titull',
        ),
    ]
