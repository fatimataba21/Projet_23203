from django.db import models

class ProductType(models.Model):
    code = models.CharField(max_length=45)
    label = models.CharField(max_length=45)
    description = models.CharField(max_length=45, null=True, blank=True)

class Product(models.Model):
    code = models.CharField(max_length=45)
    name = models.CharField(max_length=45)
    description = models.CharField(max_length=45, null=True, blank=True)
    unit_measure = models.CharField(max_length=45, null=True, blank=True)
    product_type = models.ForeignKey(ProductType, on_delete=models.SET_NULL, null=True)

class Wilaya(models.Model):
    code = models.CharField(max_length=2)
    name = models.CharField(max_length=252)

class Moughataa(models.Model):
    code = models.CharField(max_length=45)
    label = models.CharField(max_length=45)
    wilaya = models.ForeignKey(Wilaya, on_delete=models.CASCADE)

class Commune(models.Model):
    code = models.CharField(max_length=45)
    name = models.CharField(max_length=45)
    moughataa = models.ForeignKey(Moughataa, on_delete=models.CASCADE)

class PointOfSale(models.Model):
    code = models.CharField(max_length=45)
    type = models.CharField(max_length=45)
    gps_lat = models.FloatField(null=True, blank=True)
    gps_lon = models.FloatField(null=True, blank=True)
    commune = models.ForeignKey(Commune, on_delete=models.CASCADE)

class ProductPrice(models.Model):
    value = models.FloatField()
    date_from = models.DateField()
    date_to = models.DateField(null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    point_of_sale = models.ForeignKey(PointOfSale, on_delete=models.CASCADE)

class Cart(models.Model):
    code = models.CharField(max_length=45)
    name = models.CharField(max_length=45)
    description = models.CharField(max_length=45, null=True, blank=True)

class CartProducts(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart_product = models.ForeignKey(Cart, on_delete=models.CASCADE)
    weight = models.FloatField()
    date_from = models.DateField()
    date_to = models.DateField(null=True, blank=True)

# models.py
class Sale(models.Model):
    month = models.CharField(max_length=10)  # ex: "Jan", "Fév", etc.
    amount = models.FloatField()            # chiffre d'affaires ou ventes
    product_type = models.CharField(max_length=50)  # ex: "Electronique", "Alimentaire", etc.
    # ... d'autres champs éventuels ...

    def __str__(self):
        return f"{self.month} - {self.amount}"

class INPC(models.Model):
    month = models.CharField(max_length=20, unique=True)  # Mois concerné
    value = models.FloatField()  # Valeur de l'INPC
    created_at = models.DateTimeField(auto_now_add=True)  # Date d'ajout automatique

    def __str__(self):
        return f"INPC {self.month}: {self.value}"