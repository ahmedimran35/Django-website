from django.shortcuts import render,HttpResponse

# Create your views here.

def index(request):
    #return HttpResponse("this is home")
    return render(request,'index.html')

def about(request):
    #return HttpResponse("this is about page")
     return render(request,'about.html')

def educations(request):
    #return HttpResponse("this is skills page")
    return render(request,'educations.html')

def services(request):
   # return HttpResponse("this is services page")
    return render(request,'services.html')

def works(request):
    #return HttpResponse("this is works page")
     return render(request,'works.html')

def contact(request):
    #return HttpResponse("this is contact page")
    return render(request,'contact.html')

