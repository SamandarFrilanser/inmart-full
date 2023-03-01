from json import loads
from .models import (
    Product,
    Order,
    Customer,
    OrderItem
)


def cookie_cart(request) -> list:
    try:
        cart = loads(request.COOKIES.get('cart'))
    except:
        cart = {}
    items = []
    order = {
        'get_cart_items': 0,
        'get_cart_total': 0,
        'total_stock': 0
    }
    cart_items = order.get('get_cart_items')
    for i, q in cart.items():
        try:
            quantity = q.get('quantity')
            cart_items += quantity
            product = Product.objects.get(pk=int(i))
            is_stock = product.is_stock
            price = product.price
            if is_stock:
                total_stock = (price * product.stock) // 100
                total = (price - total_stock) * quantity
                order['total_stock'] += (total_stock * quantity)
            else:
                total = (product.price * quantity)
            order['get_cart_total'] += total
            order['get_cart_items'] += quantity

            item = {
                'product': {
                    'id': product.id,
                    'name': product.name,
                    'price': price,
                    'get_images': product.get_images
                },
                'quantity': quantity,
                'get_total': total
            }
            items.append(item)
        except Exception as er:
            print(er)
            pass
    return [items, order, cart_items]


def cookie_data(request) -> list:
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cart_items = order.get_cart_items
    else:
        items, order, cart_items = cookie_cart(request)
    return [cart_items, items, order]


def guest_order(data, request) -> list:
    form = data.get('form')
    phone = form.get('phone')
    username = form.get('username')
    name = form.get('name')
    email = form.get('email')
    cart_items, items, order = cookie_data(request=request)
    customer, created = Customer.objects.get_or_create(email=email)
    customer.phone = phone
    customer.username = username
    customer.name = name
    customer.save()
    order, created = Order.objects.get_or_create(
        customer=customer,
        complete=False
    )
    for item in items:
        product = Product.objects.get(pk=item.get('product').get('id'))
        OrderItem.objects.create(
            product=product,
            order=order,
            quantity=item.get('quantity')
        )
    return [order, customer]
