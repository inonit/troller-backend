# Generated by Django 2.2.1 on 2019-05-27 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dating', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='first_name',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='last_name',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='username',
            field=models.CharField(default='', max_length=255, unique=True),
            preserve_default=False,
        ),
    ]
