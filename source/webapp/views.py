from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseNotAllowed
from django.views.generic import View, TemplateView, FormView
from webapp.forms import AskForm

from webapp.models import Article
from .base_view import FormView as CustomFormView
from django.urls import reverse


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        data = Article.objects.all()
        context = {'articles': data}
        return context



class TO_Do_View(TemplateView):
    template_name = 'to_do_view.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        pk = self.kwargs.get('pk')
        article = get_object_or_404(Article, pk=pk)

        context['article'] = article
        return context


class To_Do_Update_View(FormView):
    template_name = 'update.html'
    form_class = AskForm

    def dispatch(self, request, *args, **kwargs):
        self.article = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['article'] = self.get_object()
        return context

    def get_initial(self):
        initial = {}
        for key in 'description', 'full_description', 'date', 'type':
            initial[key] = getattr(self.article, key)
        return  initial

    def form_valid(self, form):
        for key, value in form.cleaned_data.items():
            if value is not None:
                setattr(self.article, key, value)
        self.article.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('to_do_view', kwargs={'pk': self.article.pk})

    def get_object(self):
        pk = self.kwargs.get('pk')
        return get_object_or_404(Article, pk=pk)


class To_Do_Create_View(FormView):
    template_name = 'to_do_creat.html'
    form_class = AskForm

    def form_valid(self, form):
        data = {}
        for key, value in form.cleaned_data.items():
            if value is not None:
                data[key] = value
        self.article = Article.objects.create(**data)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('to_do_view', kwargs={'pk': self.article.pk})


class Delete_To_Do(TemplateView):
    template_name = 'del_to_do.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs.get('pk')
        article = get_object_or_404(Article, pk=pk)
        context['article'] = article
        return context

    def post(self, request, pk):
        article = get_object_or_404(Article, pk=pk)
        article.delete()
        return redirect('index')