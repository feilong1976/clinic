from django.shortcuts import render
from .models import Patient
from django.http import HttpResponse
from django.template.loader import get_template
from datetime import datetime
# Create your views here.
def index(request):
    template = get_template('patient/index.html')
    
    now = datetime.now()
    html = template.render(locals())
    return HttpResponse(html)

def list(request):
    template = get_template('patient/list.html')
    patients = Patient.objects.all()
    now = datetime.now()
    html = template.render(locals())
    return HttpResponse(html)

def add(request):
    template = get_template('patient/add.html')
    now = datetime.now()
    html = template.render(locals())
    return HttpResponse(html)

