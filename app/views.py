from datetime import datetime
from json import loads
from uuid import uuid5, UUID

from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import ListView

from app.models import (
    Product,
    Order,
    OrderItem,
    Category,
    News,
    ShippingAddress,
    Customer
)
from .utils import (
    cookie_data,
    guest_order
)


def home(request):
    categories = Category.objects.all()
    products = Product.objects.filter(is_active=True)
    news = News.objects.all()
    stocks = products.filter(is_stock=True)[:4]
    cart_items, items, order = cookie_data(request=request)
    context = {
        'title': 'Inmart | Bosh Sahifa',
        'products': products,
        'items': items,
        'order': order,
        'cart_items': cart_items,
        'categories': categories,
        'news': news,
        'stocks': stocks
    }
    return render(request=request, template_name='index.html', context=context)


def cart(request):
    cart_items, items, order = cookie_data(request=request)
    context = {
        'title': 'Savatcha',
        'items': items,
        'order': order,
        'cart_items': cart_items
    }
    return render(request=request, template_name='app/cart.html', context=context)


def checkout(request):
    cart_items, items, order = cookie_data(request=request)
    context = {
        'title': 'Buyurtmani rasmiylashtirish',
        'items': items,
        'order': order,
        'cart_items': cart_items
    }
    return render(request=request, template_name='app/checkout.html', context=context)


class SearchResultsView(ListView):
    model = Product
    template_name = 'app/search_results.html'
    paginate_by = 5

    def get_context_data(self, *args, **kwargs):
        query = self.request.GET.get('q')
        context = super().get_context_data(**kwargs)
        search_results = Product.objects.filter(
            Q(name__icontains=query) | Q(description__icontains=query)
        )
        cart_items, items, order = cookie_data(request=self.request)
        context['title'] = 'Izlash...'
        context['items'] = items
        context['order'] = order
        context['cart_items'] = cart_items
        context['q'] = query
        context['search_results'] = search_results
        return context


def update_item(request):
    data = loads(request.body)
    product_id = data.get('productId')
    action = data.get('action')
    counter = data.get('counter')
    customer = request.user.customer
    product = Product.objects.get(pk=product_id)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)

    order_item, created = OrderItem.objects.get_or_create(order=order, product=product)
    if counter != 0:
        order_item.quantity += counter
        order_item.save()
        return JsonResponse('Tayyor', safe=False)
    if action == 'add':
        order_item.quantity += 1
    elif action == 'remove':
        order_item.quantity -= 1
    order_item.save()
    if order_item.quantity <= 0:
        order_item.delete()
    return JsonResponse('Tayyor', safe=False)


def remove_order_items(request):
    data = loads(request.body)
    order_id = data.get('orderId')
    customer = request.user.customer
    product = Product.objects.get(pk=order_id)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    order_item, created = OrderItem.objects.get_or_create(order=order, product=product)
    order_item.delete()
    return JsonResponse('Tayyor', safe=False)


def process_order(request):
    data = loads(request.body)
    transaction_id = str(uuid5(
        namespace=UUID('f8ef53f4-6311-4b0e-8ee2-1f0aaa4908cd'),
        name=str(datetime.now()) + str(data))
    ).replace('-', '')
    form = data.get('form')
    shipping_info = data.get('shipping')
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        Customer.objects.create(
            phone=form.get('phone'),
            username=form.get('username'),
            name=form.get('name'),
            email=form.get('email'),
        )
    else:
        order, customer = guest_order(data=data, request=request)
    total = int(form.get('total'))
    order.transaction_id = transaction_id
    if total == order.get_cart_total.get('total'):
        order.complete = True
    order.save()
    ShippingAddress.objects.create(
        customer=customer,
        order=order,
        city=shipping_info.get('city'),
        district=shipping_info.get('district'),
        street_name=shipping_info.get('street_name'),
        home_number=shipping_info.get('home_number'),
        apartment_number=shipping_info.get('apartment_number'),
    )
    return JsonResponse('Tayyor', safe=False)


def stores(request):
    cart_items, items, order = cookie_data(request=request)
    context = {
        'title': "Bizning do'konlarimiz",
        'items': items,
        'order': order,
        'cart_items': cart_items
    }
    return render(request=request, template_name='app/stores.html', context=context)


def about(request):
    cart_items, items, order = cookie_data(request=request)
    context = {
        'title': 'Biz haqimizda',
        'items': items,
        'order': order,
        'cart_items': cart_items
    }
    return render(request=request, template_name='app/about.html', context=context)


def contact(request):
    cart_items, items, order = cookie_data(request=request)
    context = {
        'title': "Bog'lanish",
        'items': items,
        'order': order,
        'cart_items': cart_items
    }
    return render(request=request, template_name='app/contact.html', context=context)
