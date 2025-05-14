from django.db.models import F, Sum
from django.utils import timezone

from outflows.models import Outflow
from products.models import Product


def get_product_metrics():
    products = Product.objects.all()
    total_cost_price = sum(
        product.cost_price * product.quantity for product in products
    )
    total_selling_price = sum(
        product.selling_price * product.quantity for product in products
    )
    total_quantity = sum(product.quantity for product in products)
    total_profit = total_selling_price - total_cost_price

    return dict(
        total_cost_price=f'{total_cost_price:,.2f}',
        total_selling_price=f'{total_selling_price:,.2f}',
        total_quantity=total_quantity,
        total_profit=f'{total_profit:,.2f}',
    )


def get_sales_metrics():
    total_sales = Outflow.objects.count()
    total_products_sold = (
        Outflow.objects.aggregate(total_products_sold=Sum('quantity'))[
            'total_products_sold'
        ] or 0
    )
    total_sales_value = sum(
        outflow.quantity * outflow.product.selling_price
        for outflow in Outflow.objects.all()
    )
    total_sales_cost = sum(
        outflow.quantity * outflow.product.cost_price
        for outflow in Outflow.objects.all()
    )
    total_sales_profit = total_sales_value - total_sales_cost

    return dict(
        total_sales=total_sales,
        total_products_sold=total_products_sold,
        total_sales_value=f'{total_sales_value:,.2f}',
        total_sales_profit=f'{total_sales_profit:,.2f}',
    )


def get_sales_value_chart_data():
    today = timezone.now().date()
    dates = [str(today - timezone.timedelta(days=i)) for i in range(6, -1, -1)]
    values = []

    for date in dates:
        sales_values = (
            Outflow.objects.filter(created_at__date=date).aggregate(
                total_sales_value=Sum(
                    F('product__selling_price') * F('quantity')
                )
            )['total_sales_value'] or 0
        )
        values.append(sales_values)

    return dict(
        dates=dates,
        values=values,
    )


def get_sales_quantity_chart_data():
    today = timezone.now().date()
    dates = [str(today - timezone.timedelta(days=i)) for i in range(6, -1, -1)]
    quantities = []

    for date in dates:
        sales_quantities = Outflow.objects.filter(
            created_at__date=date
        ).count()
        quantities.append(sales_quantities)

    return dict(
        dates=dates,
        values=quantities,
    )


def get_sales_quantity_product_chart_data():
    today = timezone.now().date()
    dates = [str(today - timezone.timedelta(days=i)) for i in range(6, -1, -1)]
    quantities = []

    for date in dates:
        sales_quantities = Outflow.objects.filter(
            created_at__date=date
        ).aggregate(total_sales_quantity=Sum('quantity'))
        quantities.append(sales_quantities['total_sales_quantity'])

    return dict(
        dates=dates,
        values=quantities,
    )


def get_sales_best_product_chart_data():
    today = timezone.now().date()
    dates = [str(today - timezone.timedelta(days=i)) for i in range(6, -1, -1)]
    values = []
    product_names = []

    for date in dates:
        sales_quantities = (
            Outflow.objects.filter(created_at__date=date)
            .values('product__title')
            .annotate(total_sales_quantity=Sum('quantity'))
            .order_by('-total_sales_quantity')[:1]
        )

        if sales_quantities:
            values.append(sales_quantities[0]['total_sales_quantity'])
            product_names.append(sales_quantities[0]['product__title'])
        else:
            values.append(0)
            product_names.append('Nenhum produto')

    return dict(dates=dates, values=values, product_names=product_names)
