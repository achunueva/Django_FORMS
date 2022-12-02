from django.shortcuts import render
from . import models
from django.views import generic
# Create your views here.
from . import forms
from django.shortcuts import get_object_or_404

class Text_view(generic.ListView):
    template_name = 'text.html'
    queryset = models.Model_text.objects.all()

    def get_queryset(self):
        return models.Model_text.objects.all()

class Text_create(generic.CreateView):
    template_name = 'create.html'
    form_class = forms.Form_text
    queryset = models.Model_text.objects.all()
    success_url = '/text/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(Text_create, self).form_valid(form=form)

class Text_update(generic.UpdateView):
    template_name = 'update.html'
    form_class = forms.Form_text
    success_url = '/text/'

    def get_object(self, **kwargs):
        note_id = self.kwargs.get('id')
        return get_object_or_404(models.Model_text, id=note_id)

    def form_valid(self, form):
        return super(Text_update, self).form_valid(form=form)


class Text_delete(generic.DeleteView):
    template_name = 'delete.html'
    success_url = '/text/'

    def get_object(self, **kwargs):
        note_id = self.kwargs.get('id')
        return get_object_or_404(models.Model_text, id=note_id)