from django.shortcuts import render
from api.models import Details
from django.http import HttpResponse
import json

# Create your views here.

def details(request):
    all_details = []
    list_details = Details.objects.all()
    for item in list_details:
        first = item.first_name
        last  = item.last_name
        gender= item.gender
        all_details.append({'first':first,'last':last,'gender':gender})
    return HttpResponse(json.dumps(all_details))

def index(request):
    return render(request, 'index.html', {}) 

def final(request):
    name = request.GET['user']
    list_details = Details.objects.all()
    gender_final = ''
    for item in list_details:
        first = item.first_name
        last  = item.last_name
        gender= item.gender
        if first == name:
            gender_final = gender
            break
        else:
            gender_final = 'Enter valid name'
    return HttpResponse(gender_final)

