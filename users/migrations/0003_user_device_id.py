# Generated by Django 2.2.9 on 2020-02-12 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20200127_1754'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='device_id',
            field=models.CharField(max_length=255, null=True, unique=True, verbose_name='device id'),
        ),
    ]