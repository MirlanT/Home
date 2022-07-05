from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, phone_choices
from .forms import ProductForm, SearchForm


def index(request):
    form = SearchForm()
    products = Product.objects.order_by('category', 'phone').exclude(count=0)
    categories = get_categories()
    return render(request, 'index.html', {'products': products, 'categories': categories, 'form': form})


def detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'detail.html', {'product': product})

def get_categories():
    products = Product.objects.exclude(count=0)
    categories = []
    for product in products:
        category = str(product).split('-')
        if category[1].strip() not in categories:
            categories.append(category[1].strip())
    return categories

def create(request):
    if request.method == 'GET':
        form = ProductForm()
        return render(request, 'create.html', {'statuses': phone_choices, 'form': form})

    elif request.method == 'POST':
        form = ProductForm(data=request.POST)
        if form.is_valid():
            Product.objects.create(
                phone=form.cleaned_data['phone'],
                description=form.cleaned_data['description'],
                category=form.cleaned_data['category'],
                count=form.cleaned_data['count'],
                price=form.cleaned_data['price']
            )
            return redirect('index')
        else:
            return render(request, 'create.html', context={'form': form})


def search(request):
    categories = get_categories()
    form = SearchForm(data=request.GET)
    if form.is_valid():
        phone = form.cleaned_data['phone']
        products = Product.objects.filter(phone__contains=phone).exclude(count=0)
        return render(request, 'index.html', {'products': products, 'categories': categories, 'form': form})
    else:
        return redirect('index')


def filter_by_category(request, category):
    products = Product.objects.filter(category=category).exclude(count=0).order_by('phone')
    categories = get_categories()
    return render(request, 'filter.html', {'products': products, 'categories': categories, 'category': category})


def update(request, pk):
    product = get_object_or_404(Product, pk=pk)

    if request.method == 'GET':
        form = ProductForm(data={
            'phone': product.phone,
            'description': product.description,
            'category': product.category,
            'count': product.count,
            'price': product.price
        })
        return render(request, 'update.html', context={'form': form, 'product': product})

    if request.method == 'POST':
        form = ProductForm(data=request.POST)
        if form.is_valid():
            product.phone = form.cleaned_data['phone']
            product.description = form.cleaned_data['description']
            product.category = form.cleaned_data['category']
            product.count = form.cleaned_data['count']
            product.price = form.cleaned_data['price']
            product.save()
            return redirect('index')
        else:
            return render(request, 'update.html', context={'form': form})


def filter_by_category(request, category):
    products = Product.objects.filter(category=category).exclude(count=0).order_by('phone')
    categories = get_categories()
    return render(request, 'filter.html', {'products': products, 'categories': categories, 'category': category})


def delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    product.delete()
    return redirect('index')
