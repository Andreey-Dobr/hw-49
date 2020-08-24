from django.shortcuts import  get_object_or_404, redirect
from django.views.generic import View, TemplateView, FormView, ListView, CreateView
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


class Task_Update_View(FormView):
    template_name = 'task/update.html'
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


class Task_Create(CreateView):
    template_name = 'task/creat.html'
    form_class = AskForm
    model = TaskList

    def form_valid(self, form):
        project = get_object_or_404(Project, pk=self.kwargs.get('pk'))
        task = form.save(commit=False)
        task.project = project
        task.save()
        return redirect('task', pk=project.pk)



class Delete_Task(TemplateView):
    template_name = 'task/del_task.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs.get('pk')
        task = get_object_or_404(TaskList, pk=pk)
        context['task'] = task
        return context

    def post(self, request, pk):
        task = get_object_or_404(TaskList, pk=pk)
        task.delete()
        return redirect('project/index')