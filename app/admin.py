from django.contrib import admin

from .models import (
    Category,
    Product,
    Order,
    OrderItem,
    ShippingAddress,
    Customer,
    News
)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ['name']}


admin.site.register(Product)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)
admin.site.register(News)
