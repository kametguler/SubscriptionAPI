from django.views import generic
from subscription.models import Product


class ProductListView(generic.ListView):
    template_name = 'index.html'
    model = Product
    queryset = Product.objects.filter(status=True)


class ProductDetailView(generic.DetailView):
    template_name = 'product_details.html'
    model = Product
