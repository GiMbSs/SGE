from django.contrib import messages
from django.contrib.auth.mixins import (LoginRequiredMixin,
                                        PermissionRequiredMixin)
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView
from rest_framework import generics

from . import forms, models, serializers


class InflowListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = models.Inflow
    template_name = 'inflow_list.html'
    context_object_name = 'inflows'
    paginate_by = 10
    permission_required = 'inflows.view_inflow'

    def get_queryset(self):
        queryset = super().get_queryset()
        product = self.request.GET.get('product')
        if product:
            queryset = queryset.filter(product__title__icontains=product)
        return queryset


class InflowCreateView(
    LoginRequiredMixin, PermissionRequiredMixin, CreateView
):
    model = models.Inflow
    template_name = 'inflow_create.html'
    form_class = forms.InflowForm
    success_url = reverse_lazy('inflow_list')
    permission_required = 'inflows.add_inflow'

    def form_valid(self, form):
        messages.success(self.request, 'Entrada criada com sucesso!')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(
            self.request,
            'Erro ao criar a entrada. Verifique os dados e tente novamente.',
        )
        return super().form_invalid(form)


class InflowDetailView(
    LoginRequiredMixin, PermissionRequiredMixin, DetailView
):
    model = models.Inflow
    template_name = 'inflow_detail.html'
    context_object_name = 'inflow'
    pk_url_kwarg = 'pk'
    success_url = reverse_lazy('inflow_list')
    permission_required = 'inflows.view_inflow'


class InflowListCreateAPIView(generics.ListCreateAPIView):
    queryset = models.Inflow.objects.all()
    serializer_class = serializers.InflowSerializer


class InflowRetrieveAPIView(generics.RetrieveAPIView):
    queryset = models.Inflow.objects.all()
    serializer_class = serializers.InflowSerializer
