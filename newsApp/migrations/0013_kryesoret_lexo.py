# Generated by Django 4.1.1 on 2022-09-19 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsApp', '0012_alter_kryesoret_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='kryesoret',
            name='lexo',
            field=models.URLField(default=''),
        ),
    ]
