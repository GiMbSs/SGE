from django.contrib import messages
from django.contrib.auth.mixins import (LoginRequiredMixin,
                                        PermissionRequiredMixin)
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView
from rest_framework import generics

from core import metrics

from . import forms, models, serializers


class OutflowListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = models.Outflow
    template_name = 'outflow_list.html'
    context_object_name = 'outflows'
    paginate_by = 10
    permission_required = 'outflows.view_outflow'

    def get_queryset(self):
        queryset = super().get_queryset()
        product = self.request.GET.get('product')
        if product:
            queryset = queryset.filter(product__name__icontains=product)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sales_metrics'] = metrics.get_sales_metrics()
        return context


class OutflowCreateView(
    LoginRequiredMixin, PermissionRequiredMixin, CreateView
):
    model = models.Outflow
    template_name = 'outflow_create.html'
    form_class = forms.OutflowForm
    success_url = reverse_lazy('outflow_list')
    permission_required = 'outflows.add_outflow'

    def form_valid(self, form):
        messages.success(self.request, 'Saída registrada com sucesso!')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(
            self.request,
            'Erro ao registrar a saída. Verifique os dados e tente novamente.',
        )
        return super().form_invalid(form)


class OutflowDetailView(
    LoginRequiredMixin, PermissionRequiredMixin, DetailView
):
    model = models.Outflow
    template_name = 'outflow_detail.html'
    context_object_name = 'outflow'
    pk_url_kwarg = 'pk'
    success_url = reverse_lazy('outflow_list')
    permission_required = 'outflows.view_outflow'


class OutflowListCreateAPIView(generics.ListCreateAPIView):
    queryset = models.Outflow.objects.all()
    serializer_class = serializers.OutflowSerializer


class OutflowRetrieveAPIView(generics.RetrieveAPIView):
    queryset = models.Outflow.objects.all()
    serializer_class = serializers.OutflowSerializer
