from .models import Category


def menu_links(request):
    categories = Category.objects.all().order_by('category_name')

    return {
        'menu_links': categories
    }