from django.contrib.auth.models import User
from django.db import models


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    phone = models.CharField(max_length=15, null=True, blank=True)
    username = models.CharField(max_length=32, null=True, blank=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    email = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        verbose_name = 'Foydalanuvchi'
        verbose_name_plural = 'Foydalanuvchilar'

    def __str__(self) -> str:
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=255, db_index=True, verbose_name="Kategoriya nomi (O'zbek tilida)")
    slug = models.SlugField(max_length=255, unique=True)

    class Meta:
        verbose_name = 'Kategoriya'
        verbose_name_plural = 'Kategoriyalar'

    def __str__(self) -> str:
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Kategoriya')
    name = models.CharField(max_length=255, verbose_name="Mahsulot nomi (O'zbek tilida)")
    description = models.TextField(blank=True, verbose_name="Mahsulot haqida (O'zbek tilida)")
    image1 = models.ImageField(upload_to='products/%Y/%m', null=True, blank=True, verbose_name='1-Rasm (Majburiy)')
    image2 = models.ImageField(upload_to='products/%Y/%m', null=True, blank=True, verbose_name='2-Rasm (Majburiy emas)')
    image3 = models.ImageField(upload_to='products/%Y/%m', null=True, blank=True, verbose_name='3-Rasm (Majburiy emas)')
    price = models.IntegerField(verbose_name="Narxi (so'mda)")
    qty = models.CharField(max_length=20, verbose_name="O'lchov birligi (O'zbek tilida)")
    stock = models.IntegerField(default=0, verbose_name="Chegirma foizi")
    is_stock = models.BooleanField(default=False, editable=False)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Mahsulot'
        verbose_name_plural = 'Mahsulotlar'
        ordering = ['-created']

    def save(self, *args, **kwargs):
        if self.stock == 0:
            self.is_stock = False
        else:
            self.is_stock = True
        super(Product, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return self.name

    @property
    def get_images(self) -> dict:
        image1 = self.image1
        image2 = self.image2
        image3 = self.image3
        if image1:
            image1 = image1.url
        if image2:
            image2 = image2.url
        if image3:
            image3 = image3.url
        return {
            'image1': image1,
            'image2': image2,
            'image3': image3,
        }

    @property
    def get_price(self) -> any:
        stock = self.stock
        old_price = self.price
        price = old_price - (old_price * stock) // 100
        return {
            'price': price,
            'old_price': old_price
        }


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    date_order = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, blank=False, null=True)
    transaction_id = models.CharField(max_length=255, null=True)

    class Meta:
        verbose_name = 'Yetkazib berish'
        verbose_name_plural = 'Yetkazib berishlar'

    def __str__(self) -> str:
        return f'{self.id} {self.customer.name}'

    @property
    def get_cart_total(self) -> dict:
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total.get('total') for item in orderitems])
        total_stock = sum([item.get_total.get('total_stock') for item in orderitems])
        return {
            'total': total,
            'total_stock': total_stock
        }

    @property
    def get_cart_items(self) -> int:
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total


class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Yetkazib beriladigan mahsulot'
        verbose_name_plural = 'Yetkazib beriladigan mahsulotlar'

    def __str__(self) -> str:
        return f'{self.id} {self.product.name}'

    @property
    def get_total(self) -> dict:
        price = self.product.price
        quantity = self.quantity
        total_stock = 0
        if self.product.is_stock:
            stock = self.product.stock
            new_price = price - (price * stock) // 100
            total_stock = (price - new_price) * quantity
            price = new_price
        total = price * quantity
        return {
            'total_stock': total_stock,
            'total': total,
        }


class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    district = models.CharField(max_length=255, blank=True, null=True)
    street_name = models.CharField(max_length=255, blank=True, null=True)
    home_number = models.CharField(max_length=255, blank=True, null=True)
    apartment_number = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        verbose_name = 'Yetkazib berish manzili'
        verbose_name_plural = 'Yetkazib berish manzillari'

    def __str__(self):
        return f'{self.customer.name} | {self.city}'


class News(models.Model):
    title_uz = models.CharField(max_length=255, verbose_name="Sahifa nomi (O'zbek tilida)")
    title_ru = models.CharField(max_length=255, verbose_name="Sahifa nomi (Rus tilida)")
    image = models.ImageField(upload_to='news/%Y/%m')
    description_uz = models.TextField(verbose_name="Sahifa nomi (O'zbek tilida)")
    description_ru = models.TextField(verbose_name="Sahifa nomi (Rus tilida)")
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Yangilik'
        verbose_name_plural = 'Yangiliklar'
        ordering = ['-created']

    def __str__(self) -> str:
        return self.title_uz
