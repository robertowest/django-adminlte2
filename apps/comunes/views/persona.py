from django.views.generic.list import ListView
from apps.comunes.models.persona import Persona

# Create your views here.
class ListView(ListView ):
    model = Persona
    template_name = 'persona/index.html'
    paginate_by = 20

    # def get_queryset(self):
    #     """Recupera los últimos diez registros creados."""
    #     return Persona.objects.order_by('-created')[:10]
