from asyncio import tasks

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseNotAllowed
from django.views.generic import View, TemplateView, FormView, ListView, DetailView, CreateView, UpdateView, DeleteView
from webapp.forms import AskForm, SimpleSearchForm, ProjectForm
from django.db.models import Q
from django.utils.http import urlencode
from webapp.models import TaskList, Project
from django.urls import reverse, reverse_lazy


class ProjectListView(ListView):
    template_name = 'project/index.html'
    context_object_name = 'projects'
    model = Project
    paginate_by = 10
    paginate_orphans = 0

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        return context



class ProjectView(DetailView):
    template_name = 'project/task_view.html'
    model = Project


    def get_context_data(self,  **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class Project_Update_View(LoginRequiredMixin,UpdateView):
    model = Project
    template_name = 'project/update.html'
    form_class = ProjectForm
    context_object_name = 'project'

    def get_success_url(self):
        return reverse('project_view', kwargs={'pk': self.object.pk})


class ProjectCreate(LoginRequiredMixin,CreateView):
    template_name = 'project/creat.html'
    form_class = ProjectForm
    model = Project

    def get_success_url(self):
        return reverse('project_view', kwargs={'pk': self.object.pk})



class Delete_Project(LoginRequiredMixin,DeleteView):
    template_name = 'project/del_task.html'
    model = Project
    context_key = 'project'

    def get_success_url(self):
        return reverse('index')