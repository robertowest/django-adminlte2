from django.urls import path

from . import views

app_name = 'comunes'
urlpatterns = [
    path('personas/', views.persona.ListView.as_view(), name='index'),

    path('usuarios/',     views.usuario.ListView.as_view(), name='usuarios'),
    path('usuario/nuevo', views.usuario.CreateView.as_view(), name='usuario_create'),
    path('usuario/<int:pk>/modificar', views.usuario.UpdateView.as_view(), name='usuario_update'),
    path('usuario/<int:pk>/eliminar',  views.usuario.DeleteView.as_view(), name='usuario_delete'),
    path('usuario/<int:pk>/detalle',   views.usuario.DetailView.as_view(), name='usuario_detail'),

    # path('login/', views.usuario.LoginView.as_view(), name='login'),
    # path('logout/', views.usuario.LogoutView.as_view(), name='logout'),
]
