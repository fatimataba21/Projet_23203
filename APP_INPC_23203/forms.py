from django import forms
from .models import (
    Product, ProductType, Wilaya, Moughataa, Commune,
    PointOfSale, ProductPrice, Cart, CartProducts
)
class CartProductsForm(forms.ModelForm):
    class Meta:
        model = CartProducts
        fields = ["product", "cart_product", "weight", "date_from", "date_to"]
# ✅ Formulaire pour ProductType
class ProductTypeForm(forms.ModelForm):
    class Meta:
        model = ProductType
        fields = "__all__"

# ✅ Formulaire pour Product
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"


class WilayaForm(forms.ModelForm):
    class Meta:
        model = Wilaya
        fields = ["code", "name"]  
# ✅ Formulaire pour Moughataa
class MoughataaForm(forms.ModelForm):
    class Meta:
        model = Moughataa
        fields = "__all__"

# ✅ Formulaire pour Commune
class CommuneForm(forms.ModelForm):
    class Meta:
        model = Commune
        fields = "__all__"

# ✅ Formulaire pour PointOfSale
class PointOfSaleForm(forms.ModelForm):
    class Meta:
        model = PointOfSale
        fields = "__all__"

# ✅ Formulaire pour ProductPrice
class ProductPriceForm(forms.ModelForm):
    class Meta:
        model = ProductPrice
        fields = "__all__"
        widgets = {
            'date_from': forms.DateInput(attrs={'type': 'date'}),
            'date_to': forms.DateInput(attrs={'type': 'date'}),
        }

# ✅ Formulaire pour Cart
class CartForm(forms.ModelForm):
    class Meta:
        model = Cart
        fields = "__all__"

# ✅ Formulaire pour CartProducts
class CartProductsForm(forms.ModelForm):
    class Meta:
        model = CartProducts
        fields = "__all__"
        widgets = {
            'date_from': forms.DateInput(attrs={'type': 'date'}),
            'date_to': forms.DateInput(attrs={'type': 'date'}),
        }
