import base64
from io import BytesIO
import matplotlib.pyplot as plt
from django.shortcuts import render
from django.core.exceptions import PermissionDenied

from order.models import Order

def get_plot():
    x = [o.created for o in Order.objects.all()]
    y = []
    for el in x:
        orders_in_date = Order.objects.all().filter(created=el)
        for order in orders_in_date:
            quantity = sum([i.quantity for i in order.items.all()])
        y.append(quantity)

    plt.plot(x, y)
    buf = BytesIO()
    plt.savefig(buf, format="png")
    buf.seek(0)
    string = base64.b64encode(buf.read())
    return string.decode("utf-8")

def analyser(request):
    if not request.user.is_staff:
        raise PermissionDenied("You must be logged in as a staff to access this page.")

    orders_cost = Order.objects.values_list("cost")

    total_income = 0
    total_count = 0

    for el in orders_cost:
        total_income += el[0]
        total_count += 1

    plot = get_plot()
    return render(
        request,
        "statistic/analyse.html",
        {
            "total_income": total_income,
            "total_count": total_count,
            "plot": plot,
        },
    )

