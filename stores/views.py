from django.shortcuts import render, redirect
from .models import Store
from .forms import StoreModelForm

# Create your views here.
def store_list(request):
    context = {
        "stores": Store.objects.all()
    }
    return render(request, 'store_list.html', context)


def create_view(request):
    form = StoreModelForm()
    context = {
        "form":form
    }
    return render(request, 'create_store.html', context)


def store_detail(request,slug):
    store = Store.objects.get(slug=slug)
    context = {
        "store":store
    }
    return render(request, 'store_detail.html',context)
