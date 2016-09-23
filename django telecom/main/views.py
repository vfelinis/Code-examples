from django.shortcuts import render, render_to_response, redirect, get_object_or_404, get_list_or_404
from django.http.response import HttpResponse
from main.models import Home, Contact, Uslugi, Menu, Submenu, Mainmenu, Sale, Onas, Problem, Product
from main.forms import ContactForm
from django.core.mail import send_mail
from django.conf import settings
from django.core.mail.message import BadHeaderError
from django.http import Http404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
import feedparser

# Create your views here.

def home(request):
    args = {}
    args['onas'] = Onas.objects.all()
    args['problem'] = Problem.objects.all()
    args['sales'] = Sale.objects.all()
    args['one'] = Submenu.objects.filter(menu__isnull=True)
    args['more'] = Submenu.objects.filter(menu__isnull=False)
    args['uslugi'] = get_list_or_404(Uslugi)
    menu = get_list_or_404(Mainmenu)
    args['menu'] = menu[0]
    home = get_list_or_404(Home)
    args['home'] = home[0]
    home = get_list_or_404(Contact)
    args['contact'] = home[0]
    args['feeds'] = feedparser.parse('http://4pda.ru/feed/')
    return render(request, "main/home.html", args)

def contact(request):
    args = {}
    args['onas'] = Onas.objects.all()
    args['problem'] = Problem.objects.all()
    args['one'] = Submenu.objects.filter(menu__isnull=True)
    args['more'] = Submenu.objects.filter(menu__isnull=False)
    args['uslugi'] = get_list_or_404(Uslugi)
    menu = get_list_or_404(Mainmenu)
    args['menu'] = menu[0]
    home = get_list_or_404(Home)
    args['home'] = home[0]
    home = get_list_or_404(Contact)
    args['contact'] = home[0]
    args['feeds'] = feedparser.parse('http://4pda.ru/feed/')
    return render(request, "main/contact.html", args)

def message(request):
    onas = Onas.objects.all()
    problem = Problem.objects.all()
    menu = get_list_or_404(Mainmenu)
    home = get_list_or_404(Home)
    contact = get_list_or_404(Contact)
    form = ContactForm(request.POST or None)
    if form.is_valid():
        name = form.cleaned_data.get("name")
        phone = form.cleaned_data.get("phone")
        email = form.cleaned_data.get("sender")
        theme = form.cleaned_data.get("theme")
        message = form.cleaned_data.get("message")
        from_email = settings.EMAIL_HOST_USER
        to_email = ['sotik59@yandex.ru']
        contact_message = "Контакты: имя - %s, телефон - %s, email - %s.\nСообщение: %s"%(name, phone, email, message)
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
        "onas" : onas,
        "problem" : problem,
        "menu" : menu[0],
        "one" : Submenu.objects.filter(menu__isnull=True),
        "more" : Submenu.objects.filter(menu__isnull=False),
        "uslugi" : get_list_or_404(Uslugi),
        "home" : home[0],
        "form" : form,
        "thanks" : "Спасибо, ваша заявка отправлена!",
        "contact" : contact[0],
        "feeds" : feedparser.parse('http://4pda.ru/feed/')
        }
        return render(request, "main/form.html", context)
    context = {
    "onas" : onas,
    "problem" : problem,
    "menu" : menu[0],
    "one" : Submenu.objects.filter(menu__isnull=True),
    "more" : Submenu.objects.filter(menu__isnull=False),
    "uslugi" : get_list_or_404(Uslugi),
    "home" : home[0],
    "form" : form,
    "contact" : contact[0],
    "feeds" : feedparser.parse('http://4pda.ru/feed/')
    }
    return render(request, "main/form.html", context)

def yandex(request):
    return render_to_response("main/yandex_6d5d0749557cc726.html")

def google(request):
    return render_to_response("main/googleb106583c234d7103.html")

def get_service(request, service_id):
    args = {}
    args['onas'] = Onas.objects.all()
    args['problem'] = Problem.objects.all()
    menu = get_list_or_404(Mainmenu)
    args['menu'] = menu[0]
    args['one'] = Submenu.objects.filter(menu__isnull=True)
    args['more'] = Submenu.objects.filter(menu__isnull=False)
    args['uslugi'] = get_list_or_404(Uslugi)
    args['u'] = get_object_or_404(Uslugi, id=service_id)
    home = get_list_or_404(Home)
    args['home'] = home[0]
    home = get_list_or_404(Contact)
    args['contact'] = home[0]
    args['feeds'] = feedparser.parse('http://4pda.ru/feed/')
    return render(request, "main/service.html", args)

def another(request, url_name):
    submenu = get_object_or_404(Submenu, url=url_name)
    product = submenu.products.filter(archive=False).order_by('price')
    query = request.GET.get("q")
    if query:
        product = product.filter(
            Q(title__icontains=query) |
            Q(description__icontains=query) |
            Q(text__icontains=query))
    paginator = Paginator(product, 12) # Show 25 contacts per page
    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        products = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        products = paginator.page(paginator.num_pages)
    args = {}
    args['onas'] = Onas.objects.all()
    args['problem'] = Problem.objects.all()
    menu = get_list_or_404(Mainmenu)
    args['menu'] = menu[0]
    args['another'] = submenu
    args['products'] = products
    args['one'] = Submenu.objects.filter(menu__isnull=True)
    args['more'] = Submenu.objects.filter(menu__isnull=False)
    args['uslugi'] = get_list_or_404(Uslugi)
    home = get_list_or_404(Home)
    args['home'] = home[0]
    home = get_list_or_404(Contact)
    args['contact'] = home[0]
    args['feeds'] = feedparser.parse('http://4pda.ru/feed/')
    return render(request, "main/another.html", args)

def get_sale(request, sale_id):
    args = {}
    args['onas'] = Onas.objects.all()
    args['problem'] = Problem.objects.all()
    args['sale'] = get_object_or_404(Sale, id=sale_id)
    args['one'] = Submenu.objects.filter(menu__isnull=True)
    args['more'] = Submenu.objects.filter(menu__isnull=False)
    args['uslugi'] = get_list_or_404(Uslugi)
    menu = get_list_or_404(Mainmenu)
    args['menu'] = menu[0]
    home = get_list_or_404(Home)
    args['home'] = home[0]
    home = get_list_or_404(Contact)
    args['contact'] = home[0]
    args['feeds'] = feedparser.parse('http://4pda.ru/feed/')
    return render(request, "main/sale.html", args)

def sale(request):
    args = {}
    args['onas'] = Onas.objects.all()
    args['problem'] = Problem.objects.all()
    args['sales'] = Sale.objects.all()
    args['one'] = Submenu.objects.filter(menu__isnull=True)
    args['more'] = Submenu.objects.filter(menu__isnull=False)
    args['uslugi'] = get_list_or_404(Uslugi)
    menu = get_list_or_404(Mainmenu)
    args['menu'] = menu[0]
    home = get_list_or_404(Home)
    args['home'] = home[0]
    home = get_list_or_404(Contact)
    args['contact'] = home[0]
    args['feeds'] = feedparser.parse('http://4pda.ru/feed/')
    return render(request, "main/sales.html", args)

def get_onas(request, onas_id):
    args = {}
    args['onas_one'] = get_object_or_404(Onas, id=onas_id)
    args['onas'] = Onas.objects.all()
    args['problem'] = Problem.objects.all()
    args['sales'] = Sale.objects.all()
    args['one'] = Submenu.objects.filter(menu__isnull=True)
    args['more'] = Submenu.objects.filter(menu__isnull=False)
    args['uslugi'] = get_list_or_404(Uslugi)
    menu = get_list_or_404(Mainmenu)
    args['menu'] = menu[0]
    home = get_list_or_404(Home)
    args['home'] = home[0]
    home = get_list_or_404(Contact)
    args['contact'] = home[0]
    args['feeds'] = feedparser.parse('http://4pda.ru/feed/')
    return render(request, "main/onas.html", args)

def get_problem(request, problem_id):
    args = {}
    args['problem_one'] = get_object_or_404(Problem, id=problem_id)
    args['onas'] = Onas.objects.all()
    args['problem'] = Problem.objects.all()
    args['sales'] = Sale.objects.all()
    args['one'] = Submenu.objects.filter(menu__isnull=True)
    args['more'] = Submenu.objects.filter(menu__isnull=False)
    args['uslugi'] = get_list_or_404(Uslugi)
    menu = get_list_or_404(Mainmenu)
    args['menu'] = menu[0]
    home = get_list_or_404(Home)
    args['home'] = home[0]
    home = get_list_or_404(Contact)
    args['contact'] = home[0]
    args['feeds'] = feedparser.parse('http://4pda.ru/feed/')
    return render(request, "main/problem.html", args)

def get_product(request, product_id):
    args = {}
    args['product'] = get_object_or_404(Product, id=product_id)
    args['onas'] = Onas.objects.all()
    args['problem'] = Problem.objects.all()
    args['sales'] = Sale.objects.all()
    args['one'] = Submenu.objects.filter(menu__isnull=True)
    args['more'] = Submenu.objects.filter(menu__isnull=False)
    args['uslugi'] = get_list_or_404(Uslugi)
    menu = get_list_or_404(Mainmenu)
    args['menu'] = menu[0]
    home = get_list_or_404(Home)
    args['home'] = home[0]
    home = get_list_or_404(Contact)
    args['contact'] = home[0]
    args['feeds'] = feedparser.parse('http://4pda.ru/feed/')
    return render(request, "main/product.html", args)