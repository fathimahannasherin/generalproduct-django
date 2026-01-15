from django.shortcuts import render,get_object_or_404
from store.models import Product
from category.models import Category
from carts.models import CartItem
from carts.views import _cart_id
from django.http import HttpResponse
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Q

# Create your views here.
def store(request, category_slug=None):
    categories = None
    products =None

    if category_slug != None:
        categories = get_object_or_404(Category, slug=category_slug)
        subcategories = categories.children.all()

        if subcategories.exists():
            products = Product.objects.filter(category__in=subcategories, is_available=True).order_by('id')
        else:
            # If it's a subcategory (no children), get products for just this one
            products = Product.objects.filter(category=categories, is_available=True).order_by('id')
            product_count = products.count()
    else:
        products = Product.objects.filter(is_available=True).order_by('id')
        product_count = products.count()

    paginator = Paginator(products, 6) # Capital 'P' for the Class
    page = request.GET.get('page') # Corrected: .GET must be all uppercase
    paged_products = paginator.get_page(page)
    product_count = products.count()

    context = {
        'products': paged_products,
        'product_count' : product_count,
    }

    return render(request,'store/store.html',context)

from django.shortcuts import render, get_object_or_404

def product_detail(request, category_slug, product_slug):
    try:
    # This automatically handles the "DoesNotExist" error for you
        single_product = get_object_or_404(Product, category__slug=category_slug, slug=product_slug)
        in_cart = CartItem.objects.filter(cart__cart_id=_cart_id(request), product=single_product).exists()
    except Exception as e:
        raise e
    
    context = {
        'single_product': single_product,
        'in_cart': in_cart,
    }
    return render(request, 'store/product_detail.html', context)


def search(request):
    products = None
    product_count = 0
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            products = Product.objects.order_by('-created_date').filter(
                Q(description__icontains=keyword) | Q(product_name__icontains=keyword) | Q(category__category_name__icontains=keyword) | Q(product_code__icontains=keyword)
            )
            product_count = products.count()
        else:
            products = Product.objects.none() 

    context = {
        'products': products,
        'product_count': product_count,
    }
    return render(request, 'store/store.html', context)