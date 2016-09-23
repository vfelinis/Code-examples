# -*- coding: utf-8 -*-
# Create your views here.
from django.shortcuts import render, render_to_response, redirect, get_object_or_404, get_list_or_404
from django.http.response import HttpResponse
from main.models import Home, About, Contact, Service, Article, Social
from main.forms import ContactForm
from django.core.mail import send_mail
from django.conf import settings
from django.core.mail.message import BadHeaderError
from django.http import Http404

def test(request):
    try:
        contents = Home.objects.get(id=2)
    except Home.DoesNotExist:
        raise Http404
    return render(request, "main/home.html", {'contents' : contents})

def home(request):
    args = {}
    args['contents'] = get_object_or_404(Home, id=1)
    args['sliders'] = get_list_or_404(Service)
    args['navbar'] = get_list_or_404(Service)
    args['contacts'] = get_object_or_404(Contact, id=2)
    args['socials'] = get_list_or_404(Social)
    return render(request, "main/home.html", args)

def message(request):
	form = ContactForm(request.POST or None)
	if form.is_valid():
		theme = form.cleaned_data.get("subject")
		email = form.cleaned_data.get("sender")
		name = form.cleaned_data.get("full_name")
		text = form.cleaned_data.get("message")
		from_email = settings.EMAIL_HOST_USER
		to_email = [settings.EMAIL_HOST_USER, 'stroyintek@mail.ru']
		contact_message = "%s: %s от %s"%(name, text, email)
		try:
			send_mail(theme, 
				contact_message, 
				from_email,
				to_email, 
				fail_silently=False)
		except BadHeaderError:
			return HttpResponse('Invalid header found')
		context = { 
		"form" : form,
		"title" : "Спасибо, ваша заявка отправлена!",
		"contacts" : get_object_or_404(Contact, id=2),
		"navbar" : get_list_or_404(Service),
        "socials" : get_list_or_404(Social)
		}
		return render(request, "main/form.html", context)
	context = { 
	"form" : form,
	"contacts" : get_object_or_404(Contact, id=2),
	"navbar" : get_list_or_404(Service),
    "socials" : get_list_or_404(Social)
	}
	return render(request, "main/form.html", context)

def about(request):
    args = {}
    args['contents'] = get_object_or_404(About, id=1)
    args['contacts'] = get_object_or_404(Contact, id=2)
    args['navbar'] = get_list_or_404(Service)
    args['socials'] = get_list_or_404(Social)
    return render(request, "main/about.html", args)

def contact(request):
    args = {}
    args['contents'] = get_object_or_404(Contact, id=2)
    args['contacts'] = get_object_or_404(Contact, id=2)
    args['navbar'] = get_list_or_404(Service)
    args['socials'] = get_list_or_404(Social)
    return render(request, "main/contact.html", args)

def get_service(request, service_id):
    args = {}
    args['contents'] = get_object_or_404(Service, id=service_id)
    args['contacts'] = get_object_or_404(Contact, id=2)
    args['navbar'] = get_list_or_404(Service)
    args['links'] = get_list_or_404(Service)
    args['socials'] = get_list_or_404(Social)
    return render(request, "main/service.html", args)

def services(request):
    args = {}
    args['contents'] = get_list_or_404(Service)
    args['contacts'] = get_object_or_404(Contact, id=2)
    args['navbar'] = get_list_or_404(Service)
    args['socials'] = get_list_or_404(Social)
    return render(request, "main/services.html", args)

def articles(request):
    args = {}
    args['contents'] = Article.objects.all()
    args['contacts'] = get_object_or_404(Contact, id=2)
    args['navbar'] = get_list_or_404(Service)
    args['socials'] = get_list_or_404(Social)
    return render(request, "main/articles.html", args)

def get_article(request, article_id):
    args = {}
    args['contents'] = get_object_or_404(Article, id=article_id)
    args['contacts'] = get_object_or_404(Contact, id=2)
    args['navbar'] = get_list_or_404(Service)
    args['socials'] = get_list_or_404(Social)
    return render(request, "main/article.html", args)

def yandex(request):
    return render_to_response("main/yandex_6379745acdb3f8f4.html")

def google(request):
    return render_to_response("main/google69bbe4774885e620.html")

def yandex2(request):
    return render_to_response("main/yandex_69b37a055164dea3.html")