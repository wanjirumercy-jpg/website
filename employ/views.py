from django.shortcuts import render, redirect
from .models import Contact

# Create your views here.
def home(request):
    return render(request,'index.html')


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