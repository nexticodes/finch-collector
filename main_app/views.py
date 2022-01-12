from django.shortcuts import render
from .models import Finch
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Create your views here.
from django.http import HttpResponse

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def finches_index(request):
    finches = Finch.objects.all()
    return render(request, 'finches/index.html', {'finches': finches})

def finches_details(request, finch_id):
    finch = Finch.objects.get(id=finch_id)
    return render(request, 'finches/details.html', {'finch': finch})

class FinchCreate(CreateView):
    model = Finch
    fields = '__all__'