from django.urls import path
from django.urls import include, re_path

from .views import ProductListView, product_list_view,ProductDetailView,product_detail_view,ProductDetailSlugView

urlpatterns = [
    path('', ProductListView.as_view()),
    re_path('(?P<slug>[\w-]+)/', ProductDetailSlugView.as_view()),
]
