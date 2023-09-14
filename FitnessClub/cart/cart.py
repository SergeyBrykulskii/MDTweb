from decimal import Decimal
from django.conf import settings
from fitnessclub_core.models import GroupClass


class Cart:

    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True

    def add(self, group_class, quantity=1, update_quantity=False):
        group_class_id = str(group_class.id)
        if group_class_id not in self.cart:
            self.cart[group_class_id] = {'quantity': 0,
                                  'cost': str(group_class.cost)}
        if update_quantity:
            self.cart[group_class_id]['quantity'] = quantity
        else:
            self.cart[group_class_id]['quantity'] += quantity
        self.save()

    def remove(self, group_class):
        group_class_id = str(group_class.id)
        if group_class_id in self.cart:
            del self.cart[group_class_id]
            self.save()

    def __iter__(self):
        group_class_ids = self.cart.keys()
        group_classes = GroupClass.objects.filter(id__in=group_class_ids)
        for group_class in group_classes:
            self.cart[str(group_class.id)]['trip'] = group_class

        for item in self.cart.values():
            item['cost'] = Decimal(item['cost'])
            item['total_cost'] = item['cost'] * item['quantity']
            yield item

    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())

    def get_total_cost(self):
        return sum(Decimal(item['cost']) * item['quantity'] for item in
                   self.cart.values())

    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True
