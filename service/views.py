from django.shortcuts import render
from .models import Service
from django.views.generic import CreateView
from .forms import CreateOrderForm
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
def index(request):

    services = Service.objects.all()

    context = {
        'services': services
    }

    return render(request, 'service/index.html', context)


class CreateOrderView(CreateView, LoginRequiredMixin):
    template_name = 'service/create-order.html'
    form_class = CreateOrderForm
    success_url = '/'
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)