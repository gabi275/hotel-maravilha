from django import forms
from .models import Hospede, Reserva, Hospedagem

class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = ['hospede', 'quarto', 'data_checkin', 'data_checkout', 'valor_total', 'status']
        widgets = {
            'data_checkin': forms.DateTimeInput(format='%Y-%m-%dT%H:%M', attrs={'type': 'datetime-local', 'step': '60'}),
            'data_checkout': forms.DateTimeInput(format='%Y-%m-%dT%H:%M', attrs={'type': 'datetime-local', 'step': '60'}),
        }

    def __init__(self, *args, user=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['hospede'].queryset = Hospede.objects.filter(cadastrado_por=user) if user and user.is_authenticated else Hospede.objects.none()
        for field in ('data_checkin', 'data_checkout'):
            self.fields[field].input_formats = ['%Y-%m-%dT%H:%M', '%Y-%m-%dT%H:%M:%S', '%Y-%m-%d %H:%M:%S']

    def clean(self):
        data = super().clean()
        if data.get('data_checkin') and data.get('data_checkout') and data['data_checkout'] <= data['data_checkin']:
            self.add_error('data_checkout', 'O check-out deve ser posterior ao check-in.')
        return data

class HospedagemForm(forms.ModelForm):
    class Meta:
        model = Hospedagem
        fields = ['reserva', 'data_entrada', 'data_saida', 'finalizada']
        widgets = {
            'data_entrada': forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date'}),
            'data_saida': forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date'}),
        }

    def __init__(self, *args, user=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['reserva'].queryset = Reserva.objects.filter(cadastrado_por=user) if user and user.is_authenticated else Reserva.objects.none()
        for field in ('data_entrada', 'data_saida'):
            self.fields[field].input_formats = ['%Y-%m-%d', '%d/%m/%Y']

    def clean(self):
        data = super().clean()
        if data.get('data_entrada') and data.get('data_saida') and data['data_saida'] < data['data_entrada']:
            self.add_error('data_saida', 'A saída não pode ser anterior à entrada.')
        return data
