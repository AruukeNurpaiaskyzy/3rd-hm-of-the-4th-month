from django.shortcuts import render
from apps.base.models import Settings,About

# Create your views here.
def index(request):
    settings_all = Settings.objects.all()
    about_all = About.objects.all()
    return render(request, "index.html", {'settings_all': settings_all, 'about_all': about_all})
