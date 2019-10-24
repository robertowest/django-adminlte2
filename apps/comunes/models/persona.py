from django.db import models
from apps.comunes.models.auditoria import AuditoriaModel


class Persona(AuditoriaModel):
    class Meta:
        verbose_name = 'Persona'
        verbose_name_plural = 'Personas'
        ordering = ['apellido', 'nombre']

    def __str__(self):
        return '{}, {}'.format(self.apellido, self.nombre)

    SEXO = (('M', 'Masculino'), ('F', 'Femenino'))

    apellido = models.CharField(max_length=30, blank=False, null=False)
    nombre = models.CharField(max_length=60, blank=False, null=False)
    dni = models.CharField(max_length=8, blank=True, null=True)
    cuil = models.CharField(max_length=13, blank=True, null=True)
    sexo = models.CharField(max_length=1, choices=SEXO, default='M')
    fec_nac = models.DateField(blank=True, null=True)
