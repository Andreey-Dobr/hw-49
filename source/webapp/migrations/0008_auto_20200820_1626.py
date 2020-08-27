# Generated by Django 2.2 on 2020-08-20 10:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0007_auto_20200813_1646'),
    ]

    operations = [
        migrations.CreateModel(
            name='TaskList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, max_length=3000, null=True, verbose_name='Название')),
                ('full_description', models.TextField(max_length=3000, verbose_name='Подробное описание')),
                ('date', models.DateTimeField(max_length=25, verbose_name='data')),
                ('updated_at', models.DateTimeField(auto_now=True, max_length=25, verbose_name='Время создания')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='status', to='webapp.Status', verbose_name='статус')),
                ('type', models.ManyToManyField(related_name='type', to='webapp.Type')),
            ],
        ),
        migrations.DeleteModel(
            name='Article',
        ),
    ]