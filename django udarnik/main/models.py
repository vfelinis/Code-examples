from django.db import models
from tinymce import models as tinymce_models

# Create your models here.

class Home(models.Model):
    class Meta():
        db_table = 'Home'
        verbose_name = 'Главная'
        verbose_name_plural = 'Главная'

    title = models.CharField(max_length=250, verbose_name = "Заголовок")
    keywords = models.CharField(max_length=250)
    description = models.CharField(max_length=250)
    text = tinymce_models.HTMLField(blank=True, verbose_name = "Текст")

    def __str__(self):
        return self.title

class Contact(models.Model):
    class Meta():
        db_table = 'Contact'
        verbose_name = 'Контакты'
        verbose_name_plural = 'Контакты'

    title = models.CharField(max_length=250, verbose_name = "Заголовок")
    keywords = models.CharField(max_length=250)
    description = models.CharField(max_length=250)
    years = models.CharField(max_length=250, verbose_name = "Текущий год")
    maps = models.CharField(max_length=250, verbose_name = "Карта")
    email = models.CharField(max_length=250, verbose_name = "Почта")
    address = models.CharField(max_length=250, verbose_name = "Адрес")
    phone = tinymce_models.HTMLField(verbose_name = "Телефоны")
    text = tinymce_models.HTMLField(verbose_name = "Текст")

    def __str__(self):
        return self.title

class About(models.Model):
    class Meta():
        db_table = 'About'
        verbose_name = 'О нас'
        verbose_name_plural = 'О нас'

    title = models.CharField(max_length=250, verbose_name = "Заголовок")
    keywords = models.CharField(max_length=250)
    description = models.CharField(max_length=250)
    text = tinymce_models.HTMLField(verbose_name = "Текст")

    def __str__(self):
        return self.title

class Sale(models.Model):
    class Meta():
        db_table = 'Sale'
        verbose_name = 'Акции'
        verbose_name_plural = 'Акции'

    title = models.CharField(max_length=250, verbose_name = "Заголовок")
    archive = models.BooleanField(verbose_name = "Архив")
    keywords = models.CharField(max_length=250)
    description = models.CharField(max_length=250)
    foto = models.ImageField(blank=True, verbose_name = "Картинка")
    text = tinymce_models.HTMLField(verbose_name = "Текст")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return "/sale/%s/" % self.id

class Service(models.Model):
    class Meta():
        db_table = 'Service'
        verbose_name = 'Услуги'
        verbose_name_plural = 'Услуги'

    title = models.CharField(max_length=250, verbose_name = "Заголовок")
    keywords = models.CharField(max_length=250)
    description = models.CharField(max_length=250)
    foto = models.ImageField(blank=True, verbose_name = "Картинка")
    text = tinymce_models.HTMLField(verbose_name = "Текст")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return "/service/%s/" % self.id