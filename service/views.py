from django.shortcuts import render
from .models import Service
from django.views.generic import CreateView
from .forms import CreateOrderForm
# Create your views here.
def index(request):

    services = Service.objects.all()

    context = {
        'services': services
    }

    return render(request, 'service/index.html', context)


class CreateOrderView(CreateView):
    template_name = 'service/create-order.html'
    form_class = CreateOrderForm
    success_url = '/'
