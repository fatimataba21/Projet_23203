from django.urls import path
from . import views

urlpatterns = [
    # =========================== #
    # PAGES PRINCIPALES
    # =========================== #
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('contact/', views.contact, name='contact'),

    # =========================== #
    # LISTES DES TABLES (READ)
    # =========================== #
    path('product-types/', views.product_type_list, name='product_type_list'),
    path('products/', views.product_list, name='product_list'),
    path('wilayas/', views.wilaya_list, name='wilaya_list'),
    path('moughataas/', views.moughataa_list, name='moughataa_list'),
    path('communes/', views.commune_list, name='commune_list'),
    path('points-of-sale/', views.point_of_sale_list, name='point_of_sale_list'),
    path('product-prices/', views.product_price_list, name='product_price_list'),
    path('carts/', views.cart_list, name='cart_list'),
    path('cart-products/', views.cartproducts_list, name='cartproducts_list'),
    path('cartproducts/', views.cartproduct_list, name='cartproduct_list'),

    # =========================== #
    # EXPORT/IMPORT EXCEL GLOBAL
    # =========================== #
    path('export/', views.export_data, name='export_data'),
    path('import/', views.import_data, name='import_data'),

    # =========================== #
    # IMPORTS SPÉCIFIQUES PAR TABLE
    # =========================== #
    path('carts/import/', views.cart_import, name='cart_import'),
    path('carts/export/', views.cart_export, name='cart_export'),
    path('wilayas/import/', views.wilaya_import, name='wilaya_import'),
    path('wilayas/export/', views.wilaya_export, name='wilaya_export'),
    path('product-types/import/', views.product_type_import, name='product_type_import'),
    path('product-types/export/', views.product_type_export, name='product_type_export'),
    path('products/import/', views.product_import, name='product_import'),
    path('products/export/', views.product_export, name='product_export'),
    path('product-prices/import/', views.product_price_import, name='product_price_import'),
    path('product-prices/export/', views.product_price_export, name='product_price_export'),
    path('moughataas/import/', views.moughataa_import, name='moughataa_import'),
    path('moughataas/export/', views.moughataa_export, name='moughataa_export'),
    path('communes/import/', views.commune_import, name='commune_import'),
    path('communes/export/', views.commune_export, name='commune_export'),
    path('points-of-sale/import/', views.point_of_sale_import, name='point_of_sale_import'),
    path('points-of-sale/export/', views.point_of_sale_export, name='point_of_sale_export'),
    path('cartproducts/export/', views.cartproducts_export, name='cartproducts_export'),
    path('cartproducts/import/', views.cartproducts_import, name='cartproducts_import'),

    # =========================== #
    # CRUD - ProductType
    # =========================== #
    path('product-types/add/', views.product_type_add, name='product_type_add'),
    path('product-types/edit/<int:pk>/', views.product_type_edit, name='product_type_edit'),
    path('product-types/delete/<int:pk>/', views.product_type_delete, name='product_type_delete'),

    # =========================== #
    # CRUD - Product
    # =========================== #
    path('products/add/', views.product_add, name='product_add'),
    path('products/edit/<int:pk>/', views.product_edit, name='product_edit'),
    path('products/delete/<int:pk>/', views.product_delete, name='product_delete'),

    # =========================== #
    # CRUD - Cart
    # =========================== #
    path('carts/add/', views.cart_add, name='cart_add'),
    path('carts/edit/<int:pk>/', views.cart_edit, name='cart_edit'),
    path('carts/delete/<int:pk>/', views.cart_delete, name='cart_delete'),

    # =========================== #
    # CRUD - Wilaya
    # =========================== #
    path('wilayas/add/', views.wilaya_add, name='wilaya_add'),
    path('wilayas/edit/<int:pk>/', views.wilaya_edit, name='wilaya_edit'),
    path('wilayas/delete/<int:pk>/', views.wilaya_delete, name='wilaya_delete'),

    # =========================== #
    # CRUD - Moughataa
    # =========================== #
    path('moughataas/add/', views.moughataa_add, name='moughataa_add'),
    path('moughataas/edit/<int:pk>/', views.moughataa_edit, name='moughataa_edit'),
    path('moughataas/delete/<int:pk>/', views.moughataa_delete, name='moughataa_delete'),

    # =========================== #
    # CRUD - Commune
    # =========================== #
    path('communes/add/', views.commune_add, name='commune_add'),
    path('communes/edit/<int:pk>/', views.commune_edit, name='commune_edit'),
    path('communes/delete/<int:pk>/', views.commune_delete, name='commune_delete'),

    # =========================== #
    # CRUD - ProductPrice
    # =========================== #
    path('prices/add/', views.product_price_add, name='product_price_add'),
    path('prices/<int:pk>/edit/', views.product_price_edit, name='product_price_edit'),
    path('prices/<int:pk>/delete/', views.product_price_delete, name='product_price_delete'),

    # =========================== #
    # CRUD - PointOfSale
    # =========================== #
    path('points-of-sale/add/', views.point_of_sale_add, name='point_of_sale_add'),
    path('points-of-sale/edit/<int:pk>/', views.point_of_sale_edit, name='point_of_sale_edit'),
    path('points-of-sale/delete/<int:pk>/', views.point_of_sale_delete, name='point_of_sale_delete'),

    # =========================== #
    # CRUD - CartProducts
    # =========================== #
    path('cart-products/add/', views.cartproducts_add, name='cartproducts_add'),
    path('cart-products/edit/<int:pk>/', views.cartproducts_edit, name='cartproducts_edit'),
    path('cart-products/delete/<int:pk>/', views.cartproducts_delete, name='cartproducts_delete'),
    path('cartproducts/', views.cartproduct_list, name='cartproduct_list'),
]
