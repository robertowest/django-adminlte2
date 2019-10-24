from django.contrib.auth.models import User
from django.db import models

from apps.comunes import utils

class AuditoriaModel(models.Model):
    class Meta:
        abstract = True

    def __iter__(self):
        for field in self._meta.fields:
            yield(field.verbose_name, field.value_to_string(self))

    def meta(self):
        return self._meta

    def get_fields(self):
        """Devuelve una lista con todos los nombres de campo de la entidad."""
        fields = []

        # descarta los campos especiales y los campos sin valor
        descarte = ('id', 'active',
                    'created', 'created_by', 'updated', 'updated_by')

        for f in self._meta.fields:
            fname = f.name
            try:
                value = getattr(self, fname)
                if len(f.flatchoices) > 0:
                    value = dict(f.flatchoices).get(value)

            except:
                value = None
            if f.editable and value and f.name not in descarte:
                fields.append({'name': f.verbose_name, 'value': value, 'type': f.get_internal_type()})
        return fields

    def delete(self):
        self.active = False
        self.save()

    def hard_delete(self):
        super(AuditoriaModel, self).delete()

    def save(self, *args, **kwargs):
        user = utils.get_current_user()
        # if user and user.is_authenticated():
        if self._state.adding:
            self.created_by = user
        else:
            self.updated_by = user
        super(AuditoriaModel, self).save(*args, **kwargs)

    active     = models.BooleanField('Activo', default=1)
    created    = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=None,
                                         null=True, blank=True, editable=False,
                                         related_name='%(class)s_created')
    updated    = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(User, on_delete=None,
                                         null=True, blank=True, editable=False,
                                         related_name='%(class)s_updated')
