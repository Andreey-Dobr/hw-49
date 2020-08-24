from asyncio import tasks

from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseNotAllowed
from django.views.generic import View, TemplateView, FormView, ListView, DetailView, CreateView
from webapp.forms import AskForm, SimpleSearchForm, ProjectForm
from django.db.models import Q
from django.utils.http import urlencode
from webapp.models import TaskList, Project
from django.urls import reverse


class ProjectListView(ListView):
    template_name = 'project/index.html'
    context_object_name = 'projects'
    model = Project
    paginate_by = 10
    paginate_orphans = 0

    def get(self, request, *args, **kwargs):
        self.form = self.get_search_form()
        self.search_value = self.get_search_value()
        return super().get(request, *args, **kwargs)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['form'] = self.form
        if self.search_value:
            context['query'] = urlencode({'search': self.search_value})
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.search_value:
            query = Q(description__icontains=self.search_value) | Q(full_description=self.search_value)
            queryset = queryset.filter(query)
        return queryset

    def get_search_form(self):
        return SimpleSearchForm(self.request.GET)

    def get_search_value(self):
        if self.form.is_valid():
            return self.form.cleaned_data['search']
        return None



class ProjectView(DetailView):
    template_name = 'project/task_view.html'
    model = Project


    def get_context_data(self,  **kwargs):
        context = super().get_context_data(**kwargs)
        #tasks = self.project.tasks.all()
        #context['tasks'] = tasks
        return context



class Task_Update_View(FormView):
    template_name = 'update.html'
    form_class = AskForm

    def dispatch(self, request, *args, **kwargs):
        self.task = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['task'] = self.task
        return context

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['instance'] = self.task
        return kwargs

    def form_valid(self, form):
        self.task = form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('task_view', kwargs={'pk': self.task.pk})

    def get_object(self):
        pk = self.kwargs.get('pk')
        return get_object_or_404(TaskList, pk=pk)

class ProjectCreate(CreateView):
    template_name = 'project/creat.html'
    form_class = ProjectForm
    model = Project

    def get_success_url(self):
        return reverse('task_view', kwargs={'pk': self.object.pk})



class Delete_Project(TemplateView):
    template_name = 'project/del_task.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs.get('pk')
        project = get_object_or_404(Project, pk=pk)
        context['project'] = project
        return context

    def post(self, request, pk):
        project = get_object_or_404(Project, pk=pk)
        project.delete()
        return redirect('index')