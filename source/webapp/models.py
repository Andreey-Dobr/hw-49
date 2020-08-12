from django.db import models


STATUS_CHOICES = [
    ('new', 'новая'),
    ('in_progress', 'В процессе'),
    ('done', 'Сделано')
]

TYPE_CHOICES = [
    ('task','задача'),
    ('Bug','ошибка'),
    ('Enhancement','улучшение.')
]



class Status(models.Model):
    name = models.CharField(max_length=100,verbose_name='статус',choices=STATUS_CHOICES, null=True, blank=True,
                            default='new')

    def __str__(self):
        return self.name



class Type(models.Model):
    name = models.CharField(max_length=100, verbose_name='тип задачи',choices=TYPE_CHOICES, default='task',
                            null=True, blank=True )

    def __str__(self):
        return self.name




class Article(models.Model):

    description = models.TextField(max_length=3000, null=True, blank=True, verbose_name='Описание')
    full_description = models.TextField(max_length=3000, null=False, verbose_name='Подробное описание')
    status = models.ForeignKey('webapp.Status', related_name='status', on_delete=models.PROTECT, verbose_name='статус')
    type = models.ManyToManyField('webapp.Type', related_name='type')

    date = models.CharField(max_length=25, null=False, blank=False, verbose_name='data')
    updated_at = models.DateTimeField(max_length=25, auto_now=True, verbose_name='Время создания')

    def __str__(self):
        return "{}. {}".format(self.pk, self.description)