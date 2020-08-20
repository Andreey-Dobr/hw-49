from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseNotAllowed
from django.views.generic import View, TemplateView, FormView, ListView
from webapp.forms import AskForm, SimpleSearchForm
from django.db.models import Q
from django.utils.http import urlencode
from webapp.models import TaskList
from .base_view import FormView as CustomFormView
from django.urls import reverse


class TaskListView(ListView):
    template_name = 'index.html'
    context_object_name = 'tasks'
    model = TaskList
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


class Task_View(TemplateView):
    template_name = 'task_view.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs.get('pk')
        task = get_object_or_404(TaskList, pk=pk)
        context['task'] = task
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


class Task_Create(FormView):
    template_name = 'creat.html'
    form_class = AskForm

    def form_valid(self, form):
        self.task = form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('task_view', kwargs={'pk': self.task.pk})


class Delete_Task(TemplateView):
    template_name = 'del_task.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs.get('pk')
        task = get_object_or_404(TaskList, pk=pk)
        context['task'] = task
        return context

    def post(self, request, pk):
        task = get_object_or_404(TaskList, pk=pk)
        task.delete()
        return redirect('index')