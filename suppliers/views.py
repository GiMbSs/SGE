from django.contrib import messages
from django.contrib.auth.mixins import (LoginRequiredMixin,
                                        PermissionRequiredMixin)
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView
from rest_framework import generics

from . import forms, models, serializers


class SupplierListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = models.Supplier
    template_name = 'supplier_list.html'
    context_object_name = 'suppliers'
    paginate_by = 10
    permission_required = 'suppliers.view_supplier'

    def get_queryset(self):
        queryset = super().get_queryset()
        name = self.request.GET.get('name')
        if name:
            queryset = queryset.filter(name__icontains=name)
        return queryset


class SupplierCreateView(
    LoginRequiredMixin, PermissionRequiredMixin, CreateView
):
    model = models.Supplier
    template_name = 'supplier_create.html'
    form_class = forms.SupplierForm
    success_url = reverse_lazy('supplier_list')
    permission_required = 'suppliers.add_supplier'

    def form_valid(self, form):
        messages.success(self.request, 'Fornecedor criado com sucesso!')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(
            self.request,
            'Erro ao criar o fornecedor. Verifique os dados e tente novamente.',
        )
        return super().form_invalid(form)


class SupplierUpdateView(
    LoginRequiredMixin, PermissionRequiredMixin, UpdateView
):
    model = models.Supplier
    template_name = 'supplier_update.html'
    form_class = forms.SupplierForm
    success_url = reverse_lazy('supplier_list')
    permission_required = 'suppliers.change_supplier'

    def form_valid(self, form):
        messages.success(self.request, 'Fornecedor atualizado com sucesso!')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(
            self.request,
            'Erro ao atualizar o fornecedor. Verifique os dados e tente novamente.',
        )
        return super().form_invalid(form)


class SupplierDeleteView(
    LoginRequiredMixin, PermissionRequiredMixin, DeleteView
):
    model = models.Supplier
    template_name = 'supplier_delete.html'
    success_url = reverse_lazy('supplier_list')
    permission_required = 'suppliers.delete_supplier'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['supplier'] = self.get_object()
        return context

    def delete(self, request, *args, **kwargs):
        messages.success(request, 'Fornecedor excluído com sucesso!')
        return super().delete(request, *args, **kwargs)


class SupplierListCreateAPIView(generics.ListCreateAPIView):
    queryset = models.Supplier.objects.all()
    serializer_class = serializers.SupplierSerializer


class SupplierRetrieveUpdateDeleteAPIView(
    generics.RetrieveUpdateDestroyAPIView
):
    queryset = models.Supplier.objects.all()
    serializer_class = serializers.SupplierSerializer
