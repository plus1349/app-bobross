# Generated by Django 2.2.9 on 2020-02-25 12:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20200217_1623'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': 'user', 'verbose_name_plural': 'users'},
        ),
        migrations.AlterModelOptions(
            name='userpainting',
            options={'verbose_name': 'user painting', 'verbose_name_plural': 'user paintings'},
        ),
    ]
