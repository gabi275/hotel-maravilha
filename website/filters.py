import django_filters
from django import forms
from .models import Reserva, StatusReserva

class ReservaFilter(django_filters.FilterSet):
    hospede__nome = django_filters.CharFilter(field_name='hospede__nome', lookup_expr='icontains', label='Nome do hóspede')
    status = django_filters.ModelChoiceFilter(queryset=StatusReserva.objects.all(), label='Status')
    data_checkin = django_filters.DateFilter(field_name='data_checkin', lookup_expr='date__gte', label='Check-in a partir de', widget=forms.DateInput(attrs={'type': 'date'}))
    class Meta:
        model = Reserva
        fields = ['hospede__nome', 'status', 'data_checkin']
