from django.shortcuts import render,redirect
from django.urls import reverse
from django.core.mail import EmailMessage
from .settings import EMAIL_HOST_USER
from hotels.models import City,Country,Hotel,PartnerShipBrands
def home_page(request):
    indian = City.objects.filter(country__name='India')
    countries = Country.objects.exclude(name='India')

    return render(request,'index.html',{'local':indian,'foreign':countries})

def about_page(request):
    indian = City.objects.filter(country__name='India')
    countries = Country.objects.exclude(name='India')

    return render(request,'about.html',{'local':indian,'foreign':countries})

def service_page(request):
    indian = City.objects.filter(country__name='India')
    countries = Country.objects.exclude(name='India')

    return render(request,'service.html',{'local':indian,'foreign':countries})

def page_404(request):
    indian = City.objects.filter(country__name='India')
    countries = Country.objects.exclude(name='India')
    return render(request,'404.html',{'local':indian,'foreign':countries})

def booking_page(request):
    indian = City.objects.filter(country__name='India')
    countries = Country.objects.exclude(name='India')
    return render(request,'booking.html',{'local':indian,'foreign':countries})

def testimonial(request):
    indian = City.objects.filter(country__name='India')
    countries = Country.objects.exclude(name='India')
    return render(request,'testimonial.html',{'local':indian,'foreign':countries})

def team(request):
    indian = City.objects.filter(country__name='India')
    countries = Country.objects.exclude(name='India')
    return render(request,'team.html',{'local':indian,'foreign':countries})

def contact_page(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        number = request.POST.get('number')
        message = request.POST.get('message')
        subject = 'query'
        body = f'name: {name}\nnumber: {number}\nemail: {email}\nMessage:\n{message}'
        from_email = EMAIL_HOST_USER
        to = ['support@snoffletech.com']

        email = EmailMessage(subject, body, from_email, to)
        email.send()
        return redirect(reverse('home'))
    indian = City.objects.filter(country__name='India')
    countries = Country.objects.exclude(name='India')
    return render(request,'contact.html', {'local':indian,'foreign':countries})


def display_city(request,city_id):
    hotels = Hotel.objects.filter(city=city_id)
    indian = City.objects.filter(country__name='India')
    countries = Country.objects.exclude(name='India')
    city = City.objects.filter(id=city_id)[0]
    context={
        'hotels':hotels,
        'local':indian,
        'foreign':countries,
        'city':city
    }
    return render(request,'destination.html',context)

def display_country(request,country_id):
    # hotels = Hotel.objects.filter(city=city_id)
    indian = City.objects.filter(country__name='India')
    countries = Country.objects.exclude(name='India')
    country = Country.objects.filter(id=country_id)[0]
    cities = City.objects.filter(country=country_id)
    hotels = Hotel.objects.filter(city__in=cities)
    context={
        'hotels':hotels,
        'local':indian,
        'foreign':countries,
        'place':country
    }
    return render(request,'destination.html',context)

def ourhotels(request):
    partner = PartnerShipBrands.objects.all()
    indian = City.objects.filter(country__name='India')
    countries = Country.objects.exclude(name='India')
    return render(request,'hotels.html',{'brand':partner,  'local':indian,
        'foreign':countries,})