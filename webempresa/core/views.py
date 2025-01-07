from django.shortcuts import render

# Create your views here.
 
def home(request):
    return render(request, "core/home.html")

def about(request):
    return render(request, "core/about.html")

#def services(request): Fue trasladada al views de services 42/2:25
    #return render(request, "core/services.html")

def store(request):
    return render(request, "core/store.html")

#def contact(request): #lo traslado a la nueva app contact 1:04
    #return render(request, "core/contact.html")

#def sample (request):
    #return render(request, "core/sample.html")