from django import forms

class CadastroClienteForm(forms.Form):
    nome = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=100)
    # Outros campos do cliente
