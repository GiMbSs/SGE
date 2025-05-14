from django import forms

from .models import Brand


class BrandForm(forms.ModelForm):
    class Meta:
        model = Brand
        fields = ['name', 'description']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(
                attrs={'class': 'form-control', 'rows': 3}
            ),
        }
        labels = {
            'name': 'Nome da Marca',
            'description': 'Descrição da Marca',
        }
        help_texts = {
            'name': 'Insira o nome da marca.',
            'description': 'Insira uma descrição para a marca.',
        }
