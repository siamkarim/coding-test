from django.views import generic
from product.models import ProductVariantPrice
from product.models import Variant,Product


class CreateProductView(generic.TemplateView):
    template_name = 'products/create.html'

    def get_context_data(self, **kwargs):
        context = super(CreateProductView, self).get_context_data(**kwargs)
        variants = Variant.objects.filter(active=True).values('id', 'title')
        context['product'] = True
        context['variants'] = list(variants.all())
        return context


class TemplateView:
    template_name = 'products/list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        stocks = ProductVariantPrice.objects.filter.values('stock')
        prices = ProductVariantPrice.objects.filter.values('price')
        products = Product.objects.filter.values('id', 'title')
        context['product'] = True
        context['stock'] = list(stocks.all())
        context['price'] = list(prices.all())
        context['products'] = list(products.all())

        return context


