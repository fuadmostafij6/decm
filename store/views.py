from django.shortcuts import render, get_object_or_404
from .models import Product
from app.models import Category
from cart.views import _cart_id
from cart.models import CartItem
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
# Create your views here.


def store(request, category_slug=None):
    categories = None
    products = None

    if category_slug != None:
        categories = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(
            category=categories, is_available=True)

        paginator = Paginator(products, 2)
        page = request.GET.get('page')
        paged_products = paginator.get_page(page)
        product_count = products.count()

    else:
        products = Product.objects.filter(is_available=True).order_by('id')
        paginator = Paginator(products, 6)
        page = request.GET.get('page')
        paged_products = paginator.get_page(page)
        product_count = products.count()

    context = {
        'products': paged_products,
        'product_count': product_count,
    }

    return render(request, 'store.html', context)


def product_detail(request, category_slug, product_slug):
    try:
        single_product = Product.objects.get(
            category__slug=category_slug, slug=product_slug)

        in_cart = CartItem.objects.filter(product=single_product).exists()
    except Exception as e:
        raise e

    context = {
        'single_product': single_product,
        'in_cart': in_cart,

    }
    return render(request, 'product-detail.html', context)
