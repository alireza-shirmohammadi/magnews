# Generated by Django 2.2 on 2020-11-09 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tokenapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='token',
            name='name',
        ),
        migrations.AddField(
            model_name='token',
            name='email',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='token',
            name='token',
            field=models.CharField(default='', max_length=30),
        ),
    ]
