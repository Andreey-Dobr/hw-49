# Generated by Django 2.2 on 2020-08-12 16:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_auto_20200812_2133'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='type',
            new_name='type_old',
        ),
    ]
