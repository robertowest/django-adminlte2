from django.contrib.auth.models import User


# https://simpleisbetterthancomplex.com/tutorial/2016/07/22/how-to-extend-django-user-model.html#abstractuser
class Usuario(User):
    class Meta:
        proxy = True
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
        ordering = ['username']

    def __str__(self):
        if self.last_name and self.first_name:
            return '{}, {}'.format(self.last_name, self.first_name)
        else:
            return self.username

    def __iter__(self):
        # for field in self._meta.fields:
        #     yield (field.verbose_name, field.value_to_string(self))
        fields = ['username', 'first_name', 'last_name', 'email',
                  'is_superuser', 'is_staff', 'is_active', 'date_joined', 'last_login' ]
        for field in fields:
            f = self._meta.get_field(field)
            yield (f.verbose_name.title(), f.value_to_string(self))

    def meta(self):
        return self._meta

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('comunes:usuario_detail', args=[str(self.id)])

    def get_fields(self):
        """Devuelve una lista con todos los nombres de campo de la entidad."""
        # fields = ['username', 'first_name', 'last_name']
        import pdb;pdb.set_trace()
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