from django.contrib import admin
from .models import ProductType, Product, Wilaya, Moughataa, Commune, PointOfSale, ProductPrice, Cart, CartProducts

admin.site.register(ProductType)
admin.site.register(Product)
admin.site.register(Wilaya)
admin.site.register(Moughataa)
admin.site.register(Commune)
admin.site.register(PointOfSale)
admin.site.register(ProductPrice)
admin.site.register(Cart)
admin.site.register(CartProducts)
