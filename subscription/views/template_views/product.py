from django.shortcuts import redirect
from django.urls import reverse
from django.views import generic
from subscription.models import Product
from subscription.forms import FeedbackForm


class ProductListView(generic.ListView):
    template_name = 'index.html'
    model = Product
    queryset = Product.objects.filter(status=True)


class ProductDetailView(generic.DetailView, generic.CreateView):
    template_name = 'product_details.html'
    model = Product
    form_class = FeedbackForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product = self.get_object()
        feedbacks = product.feedbacks.filter(allowed=True)
        context['feedbacks'] = feedbacks
        return context

    def form_valid(self, form):
        feedback = form.save(commit=False)
        feedback.customer = self.request.user
        feedback.product = self.get_object()
        feedback.save()
        self.success_url = reverse("product-details", args=[feedback.product.id])
        return super().form_valid(form)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.customer = request.user
            feedback.product = self.get_object()
            feedback.save()
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_invalid(self, form):
        return redirect(reverse("product-details", args=[self.kwargs.get("pk")]))
