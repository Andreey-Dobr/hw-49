from django.contrib import admin

from webapp.models import TaskList, Status, Type, Project


class TaskAdmin(admin.ModelAdmin):
    filter_horizontal = ('type',)

admin.site.register(TaskList,TaskAdmin)
admin.site.register(Status)
admin.site.register(Type)
admin.site.register(Project)
