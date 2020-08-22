from django.shortcuts import render, reverse, get_object_or_404, redirect


def index(request):
    template_name = 'home/index.html'
    return render(request, template_name, {})


def service_booking(request):
    template_name = 'home/service-booking.html'
    return render(request, template_name, {})

def shop(request):
    template_name = 'home/shop.html'
    return render(request, template_name, {})

def shop_detail(request):
    template_name = 'home/shop-detail.html'
    return render(request, template_name, {})

def promotion(request):
    template_name = 'home/promotion.html'
    return render(request, template_name, {})

def testimonial(request):
    template_name = 'home/testimonial.html'
    return render(request, template_name, {})

def blog(request):
    template_name = 'home/blog.html'
    return render(request, template_name, {})

def blog_detail(request):
    template_name = 'home/blog-detail.html'
    return render(request, template_name, {})

def about_us(request):
    template_name = 'home/about-us.html'
    return render(request, template_name, {})

def contact(request):
    template_name = 'home/contact.html'
    return render(request, template_name, {})

def services(request):
    template_name = 'home/service.html'
    return render(request, template_name, {})

def service_details(request):
    template_name = 'home/service-details.html'
    return render(request, template_name, {})

def rent_car(request):
    template_name = 'home/rent-car.html'
    return render(request, template_name, {})