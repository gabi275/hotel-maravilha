from django import forms

class PerguntaForm(forms.Form):
    pergunta = forms.CharField(max_length=500, label="Sua pergunta", widget=forms.TextInput(attrs={"class":"form-control", "placeholder":"Ex.: Como consultar minhas reservas?", "autocomplete":"off"}))
