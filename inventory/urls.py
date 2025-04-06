from django.urls import path
from . views import ProductListCreateView,SupplierListCreateView

urlpatterns = [
    path('products/',ProductListCreateView.as_view(),name='product-list-create'),
    path('suppliers/', SupplierListCreateView.as_view(), name='supplier-list-create'),
]