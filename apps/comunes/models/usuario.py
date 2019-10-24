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

    def meta(self):
        return self._meta
