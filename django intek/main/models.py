from django.db import models

# Create your models here.
class Home(models.Model):
    class Meta():
        db_table = 'Home'

    title = models.CharField(max_length=100)
    keywords = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    text = models.TextField()

    def __str__(self):
        return self.title

class About(models.Model):
    class Meta():
        db_table = 'About'

    title = models.CharField(max_length=100)
    keywords = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    text = models.TextField()

    def __str__(self):
        return self.title

class Contact(models.Model):
    class Meta():
        db_table = 'Contact'

    title = models.CharField(max_length=100)
    keywords = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    address = models.TextField()
    phone = models.CharField(max_length=100)
    phone2 = models.CharField(max_length=100, blank=True)
    phone3 = models.CharField(max_length=100, blank=True)
    email = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Service(models.Model):
    class Meta():
        db_table = 'Service'

    title = models.CharField(max_length=100)
    keywords = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    media_file = models.FileField(blank=True)
    text = models.TextField()
    price = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.title

class Article(models.Model):
    class Meta():
        db_table = 'Article'
    title = models.CharField(max_length=100)
    keywords = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    text = models.TextField()
    source = models.CharField(max_length=200, blank=True)
    services = models.ManyToManyField(Service, related_name="services", blank=True)
    def __str__(self):
        return self.title

class Social(models.Model):
    class Meta():
        db_table = 'Social'
    name = models.CharField(max_length=250)
    url = models.CharField(max_length=250)
    def __str__(self):
        return self.name