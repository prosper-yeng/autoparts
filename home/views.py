from django.shortcuts import render, reverse, get_object_or_404, redirect


def index(request):
    template_name = 'home/index.html'
    return render(request, template_name, {})


def service_booking(request):
    template_name = 'home/service-booking.html'
    return render(request, template_name, {})

