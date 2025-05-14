import json
from decimal import Decimal

from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from . import metrics


def decimal_to_float(obj):
    if isinstance(obj, Decimal):
        return float(obj)
    if isinstance(obj, list):
        return [decimal_to_float(item) for item in obj]
    if isinstance(obj, dict):
        return {k: decimal_to_float(v) for k, v in obj.items()}
    return obj


@login_required(login_url='login')
def home(request):
    product_metrics = metrics.get_product_metrics()
    sales_metrics = metrics.get_sales_metrics()
    sales_value_chart = decimal_to_float(metrics.get_sales_value_chart_data())
    sales_quantity_chart = decimal_to_float(
        metrics.get_sales_quantity_chart_data()
    )
    sales_quantity_product = decimal_to_float(
        metrics.get_sales_quantity_product_chart_data()
    )
    sales_best_product = decimal_to_float(
        metrics.get_sales_best_product_chart_data()
    )

    context = {
        'product_metrics': product_metrics,
        'sales_metrics': sales_metrics,
        'sales_value_labels': json.dumps(sales_value_chart['dates']),
        'sales_value_data': json.dumps(sales_value_chart['values']),
        'sales_quantity_labels': json.dumps(sales_quantity_chart['dates']),
        'sales_quantity_data': json.dumps(sales_quantity_chart['values']),
        'sales_quantity_product_labels': json.dumps(
            sales_quantity_product['dates']
        ),
        'sales_quantity_product_data': json.dumps(
            sales_quantity_product['values']
        ),
        'sales_best_product_labels': json.dumps(sales_best_product['dates']),
        'sales_best_product_data': json.dumps(sales_best_product['values']),
        'sales_best_product_names': json.dumps(
            sales_best_product['product_names']
        ),
    }
    return render(request, 'home.html', context)
