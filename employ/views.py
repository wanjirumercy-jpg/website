from django.shortcuts import render, redirect
from . models import Contact, Service, Slider, Featured

from . serializers import ContactSerializer
from rest_framework import viewsets

# Create your views here.

class ContactView(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class =  ContactSerializer



def home(request):
    sliders = Slider.objects.all()
    service = Service.objects.first()
    featured = Featured.objects.all()
    context = {
        'sliders': sliders,
        'service': service,
        'feature': featured
    }
    return render(request,'index.html',context)


def portfolio(request):
    return render(request,'portfolio-details.html')

def service(request):
    return render(request,'service-details.html')

def starter(request):
    return render(request,'starter-page.html')





def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        # Create a new Contact instance
        contact = Contact(name=name, email=email, subject=subject, message=message)

        contact.save()  # Save the contact to the database

        return redirect('employ:success')  # Redirect to a success page or return a success message

    return render(request, 'index.html')  # Render the contact form template

def success(request):
    return render(request, 'success.html')  # Create a success.html template