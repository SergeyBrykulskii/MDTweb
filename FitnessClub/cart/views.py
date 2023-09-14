from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from fitnessclub_core.models import GroupClass
from .cart import Cart
from .forms import AddGroupClassForm


@require_POST
def cart_add(request, group_class_id):
    cart = Cart(request)
    group_class = get_object_or_404(GroupClass, id=group_class_id)
    form = AddGroupClassForm(request.POST)
    if form.is_valid():
        form_data = form.cleaned_data
        cart.add(group_class=group_class,
                 quantity=form_data['quantity'],
                 update_quantity=form_data['update'])
    return redirect('cart:cart_details')


def cart_remove(request, group_class_id):
    cart = Cart(request)
    group_class = get_object_or_404(GroupClass, id=group_class_id)
    cart.remove(group_class)
    return redirect('cart:cart_details')


def cart_details(request):
    cart = Cart(request)
    return render(request, 'cart_details.html', {'cart': cart})

