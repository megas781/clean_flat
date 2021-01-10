from django.shortcuts import render

# Create your views here.

def index_func(request):
    return render(request, 'master/index.html')

def contacts_func(req):
    return render(req, 'master/contacts.html')

def about_us_func(req):
    return render(req, 'master/about_us.html')