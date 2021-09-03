from django.shortcuts import render
from django.http import HttpResponse
from Gallery.models import Gallery
from Client.models import Client
from SiteInfo.models import SiteInfo

# site page path.
SINGLE_PAGE_PATH = 'Frontend/pages/'

# home page.
def index(request):
    gallerys = Gallery.objects.all()
    clients = Client.objects.all()
    site = SiteInfo.objects.all()[:1].get()
    context = {"gallerys": gallerys, "clients": clients, "site": site}
    return render(request, 'Frontend/index.html', context)


# about page.
def about(request):
    context = {}
    return render(request, SINGLE_PAGE_PATH + 'about/about.html', context)


# contact page.
def contact(request):
    context = {}
    return render(request, SINGLE_PAGE_PATH + 'contact/contact.html', context)
