from django.shortcuts import render
from django.contrib import messages
from Base.models import Contact

def home(request):
    return render(request, 'home.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        content = request.POST.get('content')
        number = request.POST.get('number')

        if not (name and 1 < len(name) < 30):
            messages.error(request, 'Invalid name')
            return render(request, 'home.html')

        if not (email and 1 < len(email) < 30):
            messages.error(request, 'Invalid email')
            return render(request, 'home.html')

        if not (number and 1 < len(number) < 13):
            messages.error(request, 'Invalid number')
            return render(request, 'home.html')

        Contact.objects.create(
            name=name,
            email=email,
            content=content,
            number=number
        )

        messages.success(request, 'Thank you! We will contact you soon.')

    return render(request, 'home.html')