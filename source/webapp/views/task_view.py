from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import  get_object_or_404, redirect
from django.views.generic import View, TemplateView, FormView, ListView, CreateView, UpdateView, DeleteView
from webapp.forms import AskForm, SimpleSearchForm
from webapp.models import TaskList, Project
from django.urls import reverse


class Task_View(TemplateView):
    template_name = 'task/task_view.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs.get('pk')
        task = get_object_or_404(TaskList, pk=pk)
        context['task'] = task
        return context


class Task_Update_View(LoginRequiredMixin,UpdateView):
    model = TaskList
    template_name = 'task/update.html'
    form_class = AskForm
    context_object_name = 'task'

    def get_success_url(self):
        return reverse('task', kwargs={'pk': self.object.project.pk})


class Task_Create(LoginRequiredMixin,CreateView):
    template_name = 'task/creat.html'
    form_class = AskForm
    model = TaskList

    def form_valid(self, form):
        project = get_object_or_404(Project, pk=self.kwargs.get('pk'))
        task = form.save(commit=False)
        task.project = project
        task.save()
        return redirect('task', pk=project.pk)



class Delete_Task(LoginRequiredMixin,DeleteView):
    model = TaskList


    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('project_view', kwargs={'pk': self.object.project.pk})