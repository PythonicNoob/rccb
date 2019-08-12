from django.shortcuts import render
from django.http import HttpResponse
from .models import Complaint, Location, Category
# Create your views here.


def home(request):
    # return HttpResponse("Hello")
    return render(request, 'category/home.html', {'complaints': Complaint.objects.all().order_by('-votes')})
