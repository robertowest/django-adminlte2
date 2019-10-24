from django.urls import reverse_lazy
from django.views.generic import DetailView, FormView, CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from apps.comunes.forms import usuario as forms
from apps.comunes.models import usuario as models

# ListView   - lista de objetos
# DetailView - objeto sobre el que opera la vista
# -----------
# FormView   - formulario con el objeto actual
# CreateView -
# UpdateView
# DeleteView

def verbose_name():
    return models.Usuario._meta.verbose_name


def view_name():
    return {'singular': models.Usuario._meta.verbose_name.title(),
            'plural': models.Usuario._meta.verbose_name_plural.title()}


class ListView(ListView):
    model = models.Usuario
    template_name = 'usuario/index.html'
    paginate_by = 20


class DetailView(DetailView):
    model = models.Usuario
    template_name = verbose_name().lower() + '/detail.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['view_name'] = view_name()
        return ctx


class FormView(FormView):
    template_name = verbose_name().lower() + '/form.html'
    # form_class = ContactForm
    success_url = reverse_lazy('comunes:usuarios')

    def form_valid(self, form):
        return super().form_valid(form)


class CreateView(CreateView):
    model = models.Usuario
    form_class = forms.UsuarioNuevoForm
    template_name = verbose_name().lower() + '/form.html'
    success_url = reverse_lazy('comunes:usuarios')

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['view_name'] = view_name()
        return ctx


class UpdateView(UpdateView):
    model = models.Usuario
    form_class = forms.UsuarioForm
    template_name = verbose_name().lower() + '/form.html'
    success_url = reverse_lazy('comunes:usuarios')

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['view_name'] = view_name()
        return ctx


class DeleteView(DeleteView):
    model = models.Usuario
    template_name = verbose_name().lower() + '/delete.html'
    success_url = reverse_lazy('comunes:usuarios')
