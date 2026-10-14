
from django.shortcuts import render, get_object_or_404
from .models import Product, Category


# ==========================================
# HOME PAGE - СҮҮЛИЙН 8 БАРАА
# ==========================================
def home(request):

    products = Product.objects.select_related(
        'category'
    ).order_by('-id')[:8]

    context = {
        'products': products,
    }

    return render(
        request,
        'store/home.html',
        context
    )


# ==========================================
# STORE PAGE - БҮХ БАРАА + CATEGORY FILTER
# ==========================================
def store(request, category_slug=None):

    # Бүх барааг авах
    products = Product.objects.select_related(
        'category'
    ).order_by('-id')

    current_category = None

    # Ангиллаар шүүх
    if category_slug:
        current_category = get_object_or_404(
            Category,
            slug=category_slug
        )

        products = products.filter(
            category=current_category
        )

    context = {
        'products': products,
        'current_category': current_category,
        'products_count': products.count(),
    }

    return render(
        request,
        'store/store.html',
        context
    )


# ==========================================
# PRODUCT DETAIL PAGE
# ==========================================
def product_detail(request, category_slug, product_slug):

    product = get_object_or_404(
        Product.objects.select_related('category'),
        category__slug=category_slug,
        slug=product_slug
    )

    context = {
        'product': product,
    }

    return render(
        request,
        'store/product_detail.html',
        context
    )
