from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from django import forms
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils import timezone
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import UserPassesTestMixin
from django_filters.views import FilterView
from .filters import ReservaFilter
from .forms import ReservaForm, HospedagemForm

from .models import (
    TipoQuarto,
    StatusReserva,
    Quarto,
    Hospede,
    Reserva,
    Hospedagem
)
class Index(TemplateView):
    template_name = "website/inicio.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["total_hospedes"] = Hospede.objects.filter(cadastrado_por=self.request.user).count() if self.request.user.is_authenticated else 0
        context["total_hospedagens"] = Hospedagem.objects.filter(cadastrado_por=self.request.user).count() if self.request.user.is_authenticated else 0
        context["total_quartos"] = Quarto.objects.count()
        context["total_reservas"] = Reserva.objects.filter(cadastrado_por=self.request.user).count() if self.request.user.is_authenticated else 0

        context["data_atual"] = timezone.localdate()

        return context


class Sobre(TemplateView):
    template_name = "website/sobre.html"


class Contato(TemplateView):
    template_name = "website/contato.html"


class GestorMixin(UserPassesTestMixin):
    """Somente staff ou membros do grupo Gerente gerenciam cadastros gerais."""
    def test_func(self):
        user = self.request.user
        return user.is_authenticated and (user.is_staff or user.groups.filter(name='Gerente').exists())

#################### Views para TipoQuarto ####################


class TipoQuartoCreate(LoginRequiredMixin, GestorMixin, SuccessMessageMixin, CreateView):
    success_message = "Registro salvo com sucesso."
    model = TipoQuarto
    fields = ["nome"]
    template_name = "website/form.html"
    success_url = reverse_lazy("tipoquarto_list")
    extra_context = {
        "titulo": "Cadastro de Tipo de Quarto",
        "botao": "Cadastrar"
    }


class TipoQuartoUpdate(LoginRequiredMixin, GestorMixin, SuccessMessageMixin, UpdateView):
    success_message = "Registro salvo com sucesso."
    model = TipoQuarto
    fields = ["nome"]
    template_name = "website/form.html"
    success_url = reverse_lazy("tipoquarto_list")
    extra_context = {
        "titulo": "Edição de Tipo de Quarto",
        "botao": "Salvar"
    }


class TipoQuartoDelete(LoginRequiredMixin, GestorMixin, DeleteView):
    model = TipoQuarto
    template_name = "website/form.html"
    success_url = reverse_lazy("tipoquarto_list")
    extra_context = {
        "titulo": "Excluir Tipo de Quarto",
        "botao": "Excluir"
    }



    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Registro excluído com sucesso.")
        return response
class TipoQuartoList(LoginRequiredMixin, ListView):
    model = TipoQuarto
    template_name = "website/listas/tipoquartos.html"


class TipoQuartoDetail(LoginRequiredMixin, DetailView):
    model = TipoQuarto
    template_name = "website/ver/tipoquarto.html"


#################### Views para StatusReserva ####################


class StatusReservaCreate(LoginRequiredMixin, GestorMixin, SuccessMessageMixin, CreateView):
    success_message = "Registro salvo com sucesso."
    model = StatusReserva
    fields = ["nome"]
    template_name = "website/form.html"
    success_url = reverse_lazy("statusreserva_list")
    extra_context = {
        "titulo": "Cadastro de Status de Reserva",
        "botao": "Cadastrar"
    }


class StatusReservaUpdate(LoginRequiredMixin, GestorMixin, SuccessMessageMixin, UpdateView):
    success_message = "Registro salvo com sucesso."
    model = StatusReserva
    fields = ["nome"]
    template_name = "website/form.html"
    success_url = reverse_lazy("statusreserva_list")
    extra_context = {
        "titulo": "Edição de Status de Reserva",
        "botao": "Salvar"
    }


class StatusReservaDelete(LoginRequiredMixin, GestorMixin, DeleteView):
    model = StatusReserva
    template_name = "website/form.html"
    success_url = reverse_lazy("statusreserva_list")
    extra_context = {
        "titulo": "Excluir Status de Reserva",
        "botao": "Excluir"
    }



    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Registro excluído com sucesso.")
        return response
class StatusReservaList(LoginRequiredMixin, ListView):
    model = StatusReserva
    template_name = "website/listas/statusreservas.html"


class StatusReservaDetail(LoginRequiredMixin, DetailView):
    model = StatusReserva
    template_name = "website/ver/statusreserva.html"


#################### Views para Quarto ####################


class QuartoCreate(LoginRequiredMixin, GestorMixin, SuccessMessageMixin, CreateView):
    success_message = "Registro salvo com sucesso."
    model = Quarto
    fields = ["numero", "tipo_quarto", "capacidade", "valor_diaria", "disponivel"]
    template_name = "website/form.html"
    success_url = reverse_lazy("quarto_list")
    extra_context = {
        "titulo": "Cadastro de Quartos",
        "botao": "Cadastrar"
    }


class QuartoUpdate(LoginRequiredMixin, GestorMixin, SuccessMessageMixin, UpdateView):
    success_message = "Registro salvo com sucesso."
    model = Quarto
    fields = ["numero", "tipo_quarto", "capacidade", "valor_diaria", "disponivel"]
    template_name = "website/form.html"
    success_url = reverse_lazy("quarto_list")
    extra_context = {
        "titulo": "Edição de Quartos",
        "botao": "Salvar"
    }


class QuartoDelete(LoginRequiredMixin, GestorMixin, DeleteView):
    model = Quarto
    template_name = "website/form.html"
    success_url = reverse_lazy("quarto_list")
    extra_context = {
        "titulo": "Excluir Quarto",
        "botao": "Excluir"
    }



    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Registro excluído com sucesso.")
        return response
class QuartoList(LoginRequiredMixin, ListView):
    model = Quarto
    template_name = "website/listas/quartos.html"

class QuartoDetail(LoginRequiredMixin, DetailView):
    model = Quarto
    template_name = "website/ver/quarto.html"


#################### Views para Hospede ####################


class HospedeCreate(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    success_message = "Registro salvo com sucesso."
    model = Hospede
    fields = ["nome", "cpf", "telefone", "email"]
    template_name = "website/form.html"
    success_url = reverse_lazy("hospede_list")
    extra_context = {
        "titulo": "Cadastro de Hóspedes",
        "botao": "Cadastrar"
    }



    def form_valid(self, form):
        form.instance.cadastrado_por = self.request.user
        return super().form_valid(form)
class HospedeUpdate(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    success_message = "Registro salvo com sucesso."
    model = Hospede
    fields = ["nome", "cpf", "telefone", "email"]
    template_name = "website/form.html"
    success_url = reverse_lazy("hospede_list")
    extra_context = {
        "titulo": "Edição de Hóspedes",
        "botao": "Salvar"
    }



    def get_queryset(self):
        return super().get_queryset().filter(cadastrado_por=self.request.user)
class HospedeDelete(LoginRequiredMixin, DeleteView):
    model = Hospede
    template_name = "website/form.html"
    success_url = reverse_lazy("hospede_list")
    extra_context = {
        "titulo": "Excluir Hóspede",
        "botao": "Excluir"
    }



    def get_queryset(self):
        return super().get_queryset().filter(cadastrado_por=self.request.user)

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Registro excluído com sucesso.")
        return response
class HospedeList(LoginRequiredMixin, ListView):
    paginate_by = 10
    model = Hospede
    template_name = "website/listas/hospedes.html"



    def get_queryset(self):
        return super().get_queryset().filter(cadastrado_por=self.request.user)
class HospedeDetail(LoginRequiredMixin, DetailView):
    model = Hospede
    template_name = "website/ver/hospede.html"


#################### Views para Reserva ####################



    def get_queryset(self):
        return super().get_queryset().filter(cadastrado_por=self.request.user)
class ReservaCreate(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    success_message = "Registro salvo com sucesso."
    model = Reserva
    form_class = ReservaForm
    template_name = "website/form.html"
    success_url = reverse_lazy("reserva_list")
    extra_context = {
        "titulo": "Cadastro de Reservas",
        "botao": "Cadastrar"
    }

    def form_valid(self, form):
        form.instance.cadastrado_por = self.request.user
        return super().form_valid(form)



    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["user"] = self.request.user
        return kwargs
class ReservaUpdate(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    success_message = "Registro salvo com sucesso."
    model = Reserva
    form_class = ReservaForm
    template_name = "website/form.html"
    success_url = reverse_lazy("reserva_list")
    extra_context = {
        "titulo": "Edição de Reservas",
        "botao": "Salvar"
    }

    def get_queryset(self):
        return super().get_queryset().filter(cadastrado_por=self.request.user)



    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["user"] = self.request.user
        return kwargs
class ReservaDelete(LoginRequiredMixin, DeleteView):
    model = Reserva
    template_name = "website/form.html"
    success_url = reverse_lazy("reserva_list")
    extra_context = {
        "titulo": "Excluir Reserva",
        "botao": "Excluir"
    }

    def get_queryset(self):
        return super().get_queryset().filter(cadastrado_por=self.request.user)



    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Registro excluído com sucesso.")
        return response
class ReservaList(LoginRequiredMixin, FilterView):
    filterset_class = ReservaFilter
    paginate_by = 10
    model = Reserva
    template_name = "website/listas/reservas.html"

    def get_queryset(self):
        return super().get_queryset().filter(cadastrado_por=self.request.user)


class ReservaDetail(LoginRequiredMixin, DetailView):
    model = Reserva
    template_name = "website/ver/reserva.html"

    def get_queryset(self):
        return super().get_queryset().filter(cadastrado_por=self.request.user)


#################### Views para Hospedagem ####################


class HospedagemCreate(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    success_message = "Registro salvo com sucesso."
    model = Hospedagem
    form_class = HospedagemForm
    template_name = "website/form.html"
    success_url = reverse_lazy("hospedagem_list")
    extra_context = {
        "titulo": "Cadastro de Hospedagens",
        "botao": "Cadastrar"
    }

    def form_valid(self, form):
        form.instance.cadastrado_por = self.request.user
        return super().form_valid(form)



    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["user"] = self.request.user
        return kwargs
class HospedagemUpdate(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    success_message = "Registro salvo com sucesso."
    model = Hospedagem
    form_class = HospedagemForm
    template_name = "website/form.html"
    success_url = reverse_lazy("hospedagem_list")
    extra_context = {
        "titulo": "Edição de Hospedagens",
        "botao": "Salvar"
    }

    def get_queryset(self):
        return super().get_queryset().filter(cadastrado_por=self.request.user)



    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["user"] = self.request.user
        return kwargs
class HospedagemDelete(LoginRequiredMixin, DeleteView):
    model = Hospedagem
    template_name = "website/form.html"
    success_url = reverse_lazy("hospedagem_list")
    extra_context = {
        "titulo": "Excluir Hospedagem",
        "botao": "Excluir"
    }

    def get_queryset(self):
        return super().get_queryset().filter(cadastrado_por=self.request.user)



    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Registro excluído com sucesso.")
        return response
class HospedagemList(LoginRequiredMixin, ListView):
    paginate_by = 10
    model = Hospedagem
    template_name = "website/listas/hospedagens.html"

    def get_queryset(self):
        return super().get_queryset().filter(cadastrado_por=self.request.user)


class HospedagemDetail(LoginRequiredMixin, DetailView):
    model = Hospedagem
    template_name = "website/ver/hospedagem.html"

    def get_queryset(self):
        return super().get_queryset().filter(cadastrado_por=self.request.user)
