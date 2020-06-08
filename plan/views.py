from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse("goold")

from .models import Plans,Students
def plans(request):
    planslist = Plans.objects.all()
    return render(request,'plan/plans.html',{'plans':planslist})

def students(request):
    studentslist = Students.objects.all()
    return render(request,'plan/students.html',{'students':studentslist})

def studentsplan(request,num):
    student = Students.objects.get(pk=num)
    planslist = student.plans_set.all()
    return render(request,'plan/plans.html',{'plans':planslist})

#def dplan(request,num):
   # plan = Plans.objects.get(pk=num)
    #return render(request,)

    pass