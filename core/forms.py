from django import forms

class CadastroClienteForm(forms.Form):
    nome = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=100)
    endereco = forms.CharField(max_length=200)
    telefone = forms.CharField(max_length=20)
