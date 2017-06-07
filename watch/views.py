from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.core.urlresolvers import reverse_lazy
from django.views.generic import View
from .models import Brand, Watch, Carousel
from django.shortcuts import render_to_response
from django.db.models import Q
import operator
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import json
from functools import reduce

# class IndexView(generic.ListView):
#     template_name = 'watch/index.html'
#     context_object_name = 'all_brands'
#
#     def get_queryset(self):
#         return Brand.objects.all()
def index_view(request):
    brand_list = Brand.objects.all()
    watch_list = Watch.objects.all()
    carousel_list = Carousel.objects.all()
    feature_list = watch_list.filter(featured=True)
    latest_list = watch_list.order_by('pub_date')[:4]
    context = {
        "watch_list": watch_list,
        "brand_list": brand_list,
        "feature_list": feature_list,
        "latest_list": latest_list,
        "carousel_list": carousel_list,
    }
    return render(request, "watch/index.html", context)

def watch_list(request):
    brand_list = Brand.objects.all()
    watch_list = Watch.objects.all()
    color_list = Watch.objects.values_list('color', flat=True).distinct()
    no_of_available = Watch.objects.all().count
    query = request.GET.get("q")
    category_query = request.GET.get("query")
    if query:
        watch_list = watch_list.filter(
            Q(name__icontains=query)|
            Q(year__icontains=query)
            ).distinct()
    page = request.GET.get('page', 1)
    paginator = Paginator(watch_list, 12)
    try:
        watch_list = paginator.page(page)
    except PageNotAnInteger:
        watch_list = paginator.page(1)
    except EmptyPage:
        watch_list = paginator.page(paginator.num_pages)


    context = {
        "watch_list": watch_list,
        "brand_list": brand_list,
        "color_list": color_list,
        "List": "List",
        "no_of_available": no_of_available
    }

    return render(request, "watch/product.html",context)

# def search_name(request):
#     if request.method == "POST":
#         search_text = request.POST['search_text']
#     else:
#         search_text = ''
#
#     watch_list = Watch.objects.filter(name__icontains=search_text)
#
#     context = {
#         "watch_list": watch_list,
#     }
#     return render(request, "watch/search_result.html",context)
#
# class detail_list(generic.DetailView):
#     model = Watch
#     template_name = 'watch/product_detail.html'



def filter(request):
    brand_list = Brand.objects.all()
    filtered_list = Watch.objects.all()

        # selected_color = request.POST.getlist('selected_color')
    selected_color = request.POST.getlist('selected_color[]')
    selected_brand = request.POST.getlist('selected_brand[]')
    filter_price_max = request.POST['filter_price_max']
    filter_price_min = request.POST['filter_price_min']
    print(filter_price_max)
    print(filter_price_min)
    filtered_list = filtered_list.filter(price__gt = filter_price_min)
    # if selected_color:
    #     filtered_list = filtered_list.filter(color__in = selected_color)
    if selected_brand:
        filtered_list = filtered_list.filter(watch_brand__name__in = selected_brand)
    if selected_color:
        filtered_list = filtered_list.filter(color__in = selected_color)

    context = {
        "filtered_list": filtered_list,
        'selected_brand': selected_brand,
    }
    return render(request, "watch/search_result.html",context)

class detail_list(generic.DetailView):
    model = Watch
    template_name = 'watch/product_detail.html'
