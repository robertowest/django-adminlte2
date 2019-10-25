from django.urls import path
from django.views.generic import TemplateView

from . import views

# --------------------------------------------
# aplicación para pruebas
# --------------------------------------------

app_name = 'xxx'
urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html'), name='home'),
    path('base/', TemplateView.as_view(template_name='adminlte/base.html'), name='base'),
    path('index/', TemplateView.as_view(template_name='adminlte/index.html'), name='index'),
    path('example/', TemplateView.as_view(template_name='adminlte/example.html'), name='example'),
    path('login/', TemplateView.as_view(template_name='adminlte/login.html'), name='login'),

    path('table/', TemplateView.as_view(template_name='adminlte/pages/index.html'), name='table'),
    path('form/', TemplateView.as_view(template_name='adminlte/pages/edit.html'), name='form'),
]
