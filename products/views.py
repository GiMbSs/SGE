from django.contrib import messages
from django.contrib.auth.mixins import (LoginRequiredMixin,
                                        PermissionRequiredMixin)
from django.urls import reverse_lazy
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)
from rest_framework import generics

from brands.models import Brand
from categories.models import Category
from core import metrics

from . import forms, models, serializers


class ProductListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = models.Product
    template_name = 'product_list.html'
    context_object_name = 'products'
    paginate_by = 10
    permission_required = 'products.view_product'

    def get_queryset(self):
        queryset = super().get_queryset()
        title = self.request.GET.get('title')
        serial_number = self.request.GET.get('serial_number')
        category = self.request.GET.get('category')
        brand = self.request.GET.get('brand')

        if title:
            queryset = queryset.filter(title__icontains=title)

        if serial_number:
            queryset = queryset.filter(serial_number__icontains=serial_number)

        if category and category.isdigit():
            queryset = queryset.filter(category__id=category)

        if brand and brand.isdigit():
            queryset = queryset.filter(brand__id=brand)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['brands'] = Brand.objects.all()
        context['product_metrics'] = metrics.get_product_metrics()
        return context


class ProductCreateView(
    LoginRequiredMixin, PermissionRequiredMixin, CreateView
):
    model = models.Product
    template_name = 'product_create.html'
    form_class = forms.ProductForm
    success_url = reverse_lazy('product_list')
    permission_required = 'products.add_product'

    def form_valid(self, form):
        messages.success(self.request, 'Produto criado com sucesso!')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(
            self.request,
            'Erro ao criar o produto. Verifique os dados e tente novamente.',
        )
        return super().form_invalid(form)


class ProductDetailView(
    LoginRequiredMixin, PermissionRequiredMixin, DetailView
):
    model = models.Product
    template_name = 'product_detail.html'
    context_object_name = 'product'
    permission_required = 'products.view_product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['product'] = self.get_object()
        return context

    def get_object(self):
        return self.model.objects.get(pk=self.kwargs['pk'])


class ProductUpdateView(
    LoginRequiredMixin, PermissionRequiredMixin, UpdateView
):
    model = models.Product
    template_name = 'product_update.html'
    form_class = forms.ProductForm
    success_url = reverse_lazy('product_list')
    permission_required = 'products.change_product'

    def form_valid(self, form):
        messages.success(self.request, 'Produto atualizado com sucesso!')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(
            self.request,
            'Erro ao atualizar o produto. Verifique os dados e tente novamente.',
        )
        return super().form_invalid(form)


class ProductDeleteView(
    LoginRequiredMixin, PermissionRequiredMixin, DeleteView
):
    model = models.Product
    template_name = 'product_delete.html'
    success_url = reverse_lazy('product_list')
    permission_required = 'products.delete_product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['product'] = self.get_object()
        return context

    def delete(self, request, *args, **kwargs):
        messages.success(request, 'Produto excluído com sucesso!')
        return super().delete(request, *args, **kwargs)


class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer


class ProductRetrieveUpdateDeleteAPIView(
    generics.RetrieveUpdateDestroyAPIView
):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer
