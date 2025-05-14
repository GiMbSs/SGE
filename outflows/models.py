from django.db import models

from products.models import Product


class Outflow(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='outflows'
    )
    quantity = models.IntegerField(default=0)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return str(self.product)
