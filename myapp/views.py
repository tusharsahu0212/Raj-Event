from django.shortcuts import render
from django.core.mail import send_mail

from myapp.models import Images,Videos

# Create your views here.

def index(request):
    return render(request,'index.html')


def contact(request):
    if request.method == "POST":
        
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')

        # print(name)
        # print(email)
        # print(phone)
        # print(desc)
        if not name and not phone:
            send_mail(
            'Raj Event',
            'Name: '+name+'\nEmail: '+email+'\nPhone Number: '+phone+'\nMessage: '+desc,
            'rajeventkacostumer@gmail.com',
            ['tusharsahu0212@gmail.com'],
            fail_silently=False,
            )
        
    return render(request,'contact.html')

def services(request):
    return render(request,'service.html')

def image(request):

    imges = Images.objects.all()

    return render(request,'image.html',{'img1s':imges})

def video(request):

    vids = Videos.objects.all()

    return render(request,'video.html',{'vids':vids})