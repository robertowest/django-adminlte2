from django import forms
from django.forms import ModelForm

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, Div, Field

from apps.comunes.models.usuario import Usuario

# Crispy Forms Layout Helpers
# https://django-crispy-forms.readthedocs.io/en/latest/layouts.html


class UsuarioNuevoForm(ModelForm):
    class Meta:
        model = Usuario
        fields = ['username', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Div(
                'username',
                'password',
                css_class='box-body',
            ),
            Div(
                Submit('submit', 'Agregar', css_class='btn btn-primary pull-right'),
                css_class='box-footer',
            ),
        )


class UsuarioForm(ModelForm):
    # username = forms.CharField(widget=forms.TextInput(attrs={'readonly': 'readonly'}))

    class Meta:
        model = Usuario
        fields = '__all__'
        labels = {
            'is_superuser': '¿Es admin?',
            'is_staff': '¿Es empleado?',
        }
        help_texts = {
            'username': '',
        }
        widgets = {
            'password': forms.PasswordInput(),
        }

    def __init__(self, *args, **kwargs):
        super(UsuarioForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Div(
                # Field('username', template='my_field_template.html', readonly=True),
                # Row(
                #     Column('username', css_class='form-group col-md-4 mb-0', readonly=True),
                #     Column('password', css_class='form-group col-md-8 mb-0'),
                #     css_class='form-row'
                # ),
                Row(
                    Column('first_name', css_class='form-group col-md-6 mb-0'),
                    Column('last_name', css_class='form-group col-md-6 mb-0'),
                    css_class='form-row'
                ),
                'email',
                'is_superuser',
                'is_staff',
                'is_active',
                Row(
                    Column('date_joined', css_class='form-group col-md-6 mb-0'),
                    Column('last_login', css_class='form-group col-md-6 mb-0'),
                    css_class='form-row'
                ),
                'groups',
                'user_permissions',
                css_class='box-body',
            ),
            Div(
                Submit('submit', 'Actualizar', css_class='btn btn-primary pull-right'),
                css_class='box-footer',
            ),
        )
