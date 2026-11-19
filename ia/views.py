from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import FormView
from .forms import PerguntaForm
from .services import responder_com_ia


class AssistenteView(LoginRequiredMixin, FormView):
    template_name = 'ia/assistente.html'
    form_class = PerguntaForm

    def form_valid(self, form):
        context = self.get_context_data(form=form)
        context['pergunta'] = form.cleaned_data['pergunta']
        context['resposta'], context['ia_generativa'] = responder_com_ia(context['pergunta'], self.request.user)
        return self.render_to_response(context)
