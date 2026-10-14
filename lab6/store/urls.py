
from django.urls import path
from django.views.generic import RedirectView
from . import views

urlpatterns = [
    # Home
    path('', views.home, name='home'),

    # Store
    path('store/', views.store, name='store'),

    # Category filter
    path(
        'store/category/<slug:category_slug>/',
        views.store,
        name='products_by_category'
    ),

    # Old product URL -> New product URL
    path(
        'store/category/<slug:category_slug>/<slug:product_slug>/',
        RedirectView.as_view(
            pattern_name='product_detail',
            permanent=True
        ),
        name='old_product_detail'
    ),

    # New short product URL
    path(
        '<slug:category_slug>/<slug:product_slug>/',
        views.product_detail,
        name='product_detail'
    ),
]
