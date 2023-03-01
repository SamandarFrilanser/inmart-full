from django.urls import path

from .views import (
    home,
    stores,
    about,
    contact,
    checkout,
    cart,
    update_item,
    remove_order_items,
    process_order,
    SearchResultsView
)

app_name = 'stores'

urlpatterns = [
    path('', home, name='home'),
    path('stores/', stores, name='stores'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('checkout/', checkout, name='checkout'),
    path('cart/', cart, name='cart'),
    path('update-item/', update_item, name='update-item'),
    path('remove-order-items/', remove_order_items, name='remove-order-items'),
    path('process-order/', process_order, name='process-order'),
    path('search/', SearchResultsView.as_view(), name='search'),
]
