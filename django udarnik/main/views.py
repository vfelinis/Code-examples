from django.shortcuts import render, render_to_response
from django.http.response import HttpResponse
from django.conf import settings
import os
from main.models import Home, Contact, About, Sale, Service
from main.forms import ContactForm
from django.core.mail import send_mail
from django.core.mail.message import BadHeaderError

# Create your views here.

def home(request):
    home = Home.objects.all()
    contact = Contact.objects.all()
    args = {}
    args['home'] = home[0]
    args['contact'] = contact[0]
    args['services'] = Service.objects.all()
    args['sales'] = Sale.objects.exclude(foto='').filter(archive=False)
    return render(request, "main/home.html", args)

def contact(request):
    contact = Contact.objects.all()
    args = {}
    args['contact'] = contact[0]
    args['services'] = Service.objects.all()
    return render(request, "main/contact.html", args)

def about(request):
    about = About.objects.all()
    contact = Contact.objects.all()
    args = {}
    args['about'] = about[0]
    args['contact'] = contact[0]
    args['services'] = Service.objects.all()
    return render(request, "main/about.html", args)

def message(request):
    contact = Contact.objects.all()
    form = ContactForm(request.POST or None)
    if form.is_valid():
        name = form.cleaned_data.get("name")
        phone = form.cleaned_data.get("phone")
        email = form.cleaned_data.get("sender")
        theme = form.cleaned_data.get("theme")
        message = form.cleaned_data.get("message")
        from_email = settings.EMAIL_HOST_USER
        to_email = ['stiekloff@mail.ru']
        contact_message = "Тема: %s\nКонтакты: имя - %s, телефон - %s, email - %s\nСообщение: %s"%(theme, name, phone, email, message)
        try:
            send_mail(theme, 
                contact_message, 
                from_email,
                to_email, 
                fail_silently=False)
        except BadHeaderError:
            return HttpResponse('Invalid header found')
        form = ContactForm()
        context = {
        "services" : Service.objects.all(),
        "form" : form,
        "thanks" : "Спасибо, ваша заявка отправлена!",
        "contact" : contact[0],
        }
        return render(request, "main/form.html", context)
    context = {
    "services" : Service.objects.all(),
    "form" : form,
    "contact" : contact[0],
    }
    return render(request, "main/form.html", context)

def sales(request):
    contact = Contact.objects.all()
    args = {}
    args['contact'] = contact[0]
    args['services'] = Service.objects.all()
    args['sales'] = Sale.objects.filter(archive=False)
    return render(request, "main/sales.html", args)

def get_sale(request, sale_id):
    contact = Contact.objects.all()
    sales = Sale.objects.filter(archive=False)
    args = {}
    args['contact'] = contact[0]
    args['services'] = Service.objects.all()
    args['sale'] = sales.get(pk = sale_id)
    return render(request, "main/sale.html", args)

def get_service(request, service_id):
    contact = Contact.objects.all()
    args = {}
    args['contact'] = contact[0]
    args['services'] = Service.objects.all()
    args['service'] = Service.objects.get(pk = service_id)
    return render(request, "main/service.html", args)

def yandex(request):
    return render_to_response("main/yandex_480de624f7674cc6.html")

def google(request):
    return render_to_response("main/google4ebc355ce8034adc.html")