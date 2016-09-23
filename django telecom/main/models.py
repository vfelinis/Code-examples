from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.

class Home(models.Model):
    class Meta():
        db_table = 'Home'
        verbose_name = 'Главная'
        verbose_name_plural = 'Главная'

    title = models.CharField(max_length=250)
    keywords = models.CharField(max_length=250)
    description = models.CharField(max_length=250)
    years = models.CharField(max_length=250)
    text = RichTextUploadingField()

    def __str__(self):
        return self.title

class Contact(models.Model):
    class Meta():
        db_table = 'Contact'
        verbose_name = 'Контакты'
        verbose_name_plural = 'Контакты'

    title = models.CharField(max_length=250)
    keywords = models.CharField(max_length=250)
    description = models.CharField(max_length=250)
    phone = RichTextUploadingField()
    email = RichTextUploadingField()
    vkontakte = models.CharField(max_length=250, blank=True)
    text = RichTextUploadingField(blank=True)
    address_1 = RichTextUploadingField(blank=True)
    address_1_map = models.CharField(max_length=250,blank=True)
    address_1_foto = models.ImageField(blank=True)
    address_2 = RichTextUploadingField(blank=True)
    address_2_map = models.CharField(max_length=250,blank=True)
    address_2_foto = models.ImageField(blank=True)
    address_3 = RichTextUploadingField(blank=True)
    address_3_map = models.CharField(max_length=250,blank=True)
    address_3_foto = models.ImageField(blank=True)
    address_4 = RichTextUploadingField(blank=True)
    address_4_map = models.CharField(max_length=250,blank=True)
    address_4_foto = models.ImageField(blank=True)

    def __str__(self):
        return self.title

class Menu(models.Model):
    class Meta():
        db_table = 'Menu'
        verbose_name = 'Группа для своих пунктов меню'
        verbose_name_plural = 'Группа для своих пунктов меню'

    title = models.CharField(max_length=250)

    def __str__(self):
        return self.title

class Submenu(models.Model):
    class Meta():
        db_table = 'Submenu'
        verbose_name = 'Свои пункты меню'
        verbose_name_plural = 'Свои пункты меню'

    title = models.CharField(max_length=250)
    keywords = models.CharField(max_length=250)
    description = models.CharField(max_length=250)
    url = models.CharField(max_length=250, unique=True)
    menu = models.ForeignKey(Menu, blank=True, null=True, on_delete=models.SET_NULL)
    text = RichTextUploadingField(blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return "/another/%s/" % self.url

class Uslugi(models.Model):
    class Meta():
        db_table = 'Uslugi'
        verbose_name = 'Цены на ремонт'
        verbose_name_plural = 'Цены на ремонт'

    title = models.CharField(max_length=250)
    keywords = models.CharField(max_length=250)
    description = models.CharField(max_length=250)
    foto = models.ImageField()
    text = RichTextUploadingField()

    def __str__(self):
        return self.title

class Mainmenu(models.Model):
    class Meta():
        db_table = 'Mainmenu'
        verbose_name = 'Названия основных пунктов меню'
        verbose_name_plural = 'Названия основных пунктов меню'

    home = models.CharField(max_length=250)
    uslugi = models.CharField(max_length=250)
    sale = models.CharField(max_length=250)
    zadat_vopros = models.CharField(max_length=250)
    o_nas = models.CharField(max_length=250)
    contact = models.CharField(max_length=250)

    def __str__(self):
        return self.home

class Sale(models.Model):
    class Meta():
        db_table = 'Sale'
        verbose_name = 'Акции'
        verbose_name_plural = 'Акции'

    title = models.CharField(max_length=250)
    keywords = models.CharField(max_length=250)
    description = models.CharField(max_length=250)
    foto = models.ImageField()
    text = RichTextUploadingField(blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return "/sale/%s/" % self.id

class Onas(models.Model):
    class Meta():
        db_table = 'Onas'
        verbose_name = 'О нас'
        verbose_name_plural = 'О нас'

    title = models.CharField(max_length=250)
    keywords = models.CharField(max_length=250)
    description = models.CharField(max_length=250)
    text = RichTextUploadingField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return "/o_nas/%s/" % self.id

class Problem(models.Model):
    class Meta():
        db_table = 'Problem'
        verbose_name = 'Проблемы'
        verbose_name_plural = 'Проблемы'

    title = models.CharField(max_length=250)
    keywords = models.CharField(max_length=250)
    description = models.CharField(max_length=250)
    icon = models.ImageField()
    text = RichTextUploadingField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return "/problem/%s/" % self.id

class Product(models.Model):
    class Meta():
        db_table = 'Product'
        verbose_name = 'Товары'
        verbose_name_plural = 'Товары'

    title = models.CharField(max_length=250)
    keywords = models.CharField(max_length=250)
    description = models.CharField(max_length=250)
    archive = models.BooleanField()
    category = models.ForeignKey(Submenu, related_name='products', blank=True, null=True, on_delete=models.SET_NULL)
    price = models.IntegerField()
    foto = models.ImageField()
    text = RichTextUploadingField()
    price_on_new = RichTextUploadingField(blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return "/product/%s/" % self.id