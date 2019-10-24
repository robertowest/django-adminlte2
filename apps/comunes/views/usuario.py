from django.urls import reverse_lazy
from django.views.generic import DetailView, FormView, CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from apps.comunes.models.usuario import Usuario

# ListView   - lista de objetos
# DetailView - objeto sobre el que opera la vista
# -----------
# FormView   - formulario con el objeto actual
# CreateView -
# UpdateView
# DeleteView

class ListView(ListView):
    model = Usuario
    template_name = 'usuario/index.html'
    paginate_by = 20


class DetailView(DetailView):
    model = Usuario
    template_name = model._meta.verbose_name.lower() + '/detail.html'


class FormView(FormView):
    template_name = Usuario._meta.verbose_name.lower() + '/form.html'
    # form_class = ContactForm
    success_url = reverse_lazy('comunes:usuarios')

    def form_valid(self, form):
        return super().form_valid(form)


class CreateView(CreateView):
    model = Usuario
    template_name = model._meta.verbose_name.lower() + '/form.html'
    fields = ['username', 'first_name', 'last_name']


class UpdateView(UpdateView):
    model = Usuario
    template_name = model._meta.verbose_name.lower() + '/form_horizontal.html'
    fields = ['username', 'first_name', 'last_name']
    # template_name_suffix = '_update_form'


class DeleteView(DeleteView):
    model = Usuario
    template_name = model._meta.verbose_name.lower() + '/delete.html'
    success_url = reverse_lazy('comunes:usuarios')
