# Generated by Django 4.0.3 on 2022-06-10 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsApp', '0006_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='kryesore',
            field=models.BooleanField(default=False),
        ),
    ]
