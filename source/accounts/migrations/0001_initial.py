# Generated by Django 2.2 on 2020-09-14 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='user_pics', verbose_name='Аватар')),
                ('profile', models.EmailField(blank=True, max_length=254, null=True)),
                ('about', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
