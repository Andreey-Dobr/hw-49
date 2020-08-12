from django.contrib import admin

from webapp.models import Article, Status, Type


class ArticleAdmin(admin.ModelAdmin):
    filter_horizontal = ('type',)

admin.site.register(Article,ArticleAdmin)
admin.site.register(Status)
admin.site.register(Type)
