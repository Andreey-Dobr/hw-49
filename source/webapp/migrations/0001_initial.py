# Generated by Django 2.2 on 2020-08-12 11:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, choices=[('new', 'новая'), ('in_progress', 'В процессе'), ('done', 'Сделано')], default='new', max_length=100, null=True, verbose_name='статус')),
            ],
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, choices=[('task', 'задача'), ('Bug', 'ошибка'), ('Enhancement', 'улучшение.')], default='task', max_length=100, null=True, verbose_name='тип задачи')),
            ],
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, max_length=3000, null=True, verbose_name='Описание')),
                ('full_description', models.TextField(max_length=3000, verbose_name='Подробное описание')),
                ('date', models.CharField(max_length=25, verbose_name='data')),
                ('updated_at', models.DateTimeField(auto_now=True, max_length=25, verbose_name='Время создания')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='status', to='webapp.Status', verbose_name='статус')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='type', to='webapp.Type', verbose_name='тип задачи')),
            ],
        ),
    ]
