from django import forms
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.urls import reverse_lazy
from django.views.generic.edit import FormView

class RecuperarUsuarioForm(forms.Form):
    email = forms.EmailField(label='E-mail cadastrado')

class RecuperarUsuario(FormView):
    template_name = 'website/form.html'
    form_class = RecuperarUsuarioForm
    success_url = reverse_lazy('login')
    extra_context = {'titulo': 'Recuperar usuário', 'botao': 'Enviar'}

    def form_valid(self, form):
        email = form.cleaned_data['email']
        nomes = list(get_user_model().objects.filter(email__iexact=email, is_active=True).values_list('username', flat=True))
        if nomes:
            send_mail('Recuperação de usuário - Hotel Maravilha', 'Seu(s) usuário(s): ' + ', '.join(nomes), settings.DEFAULT_FROM_EMAIL, [email], fail_silently=False)
        messages.success(self.request, 'Se o e-mail estiver cadastrado, você receberá as instruções.')
        return super().form_valid(form)
