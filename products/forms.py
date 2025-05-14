from django import forms

from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'title',
            'cost_price',
            'selling_price',
            'serial_number',
            'supplier',
            'brand',
            'category',
            'quantity',
            'description',
            'image',
        ]
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'cost_price': forms.NumberInput(attrs={'class': 'form-control'}),
            'selling_price': forms.NumberInput(
                attrs={'class': 'form-control'}
            ),
            'serial_number': forms.TextInput(attrs={'class': 'form-control'}),
            'supplier': forms.Select(attrs={'class': 'form-control'}),
            'brand': forms.Select(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(
                attrs={'class': 'form-control', 'rows': 3}
            ),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'title': 'Nome do Produto',
            'selling_price': 'Preço de Venda',
            'cost_price': 'Preço de Custo',
            'serial_number': 'Número de Série',
            'supplier': 'Fornecedor',
            'brand': 'Marca do Produto',
            'category': 'Categoria do Produto',
            'quantity': 'Quantidade do Produto',
            'description': 'Descrição do Produto',
            'image': 'Imagem do Produto',
        }
