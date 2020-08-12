from django.contrib import admin

from webapp.models import Article, Status, Type


class ArticleAdmin(admin.ModelAdmin):
    filter_horizontal = ('status',)

admin.site.register(Article)

admin.site.register(Status)
admin.site.register(Type)
