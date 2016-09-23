from django.contrib import admin
from main.models import Home, Contact, About, Sale, Service
# Register your models here.

class MyAdmin(admin.ModelAdmin):
    class Media:
        js = [
            '/static/static_root/grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js',
            '/static/static_root/grappelli/tinymce_setup/tinymce_setup.js',
        ]

class SaleModelAdmin(admin.ModelAdmin):
	list_display = ["title", "archive"]
	list_filter = ["archive"]
	search_fields = ["title", "description", "text"]
	list_editable = ["archive"]
	class Meta:
		model = Sale

admin.site.register(Home)
admin.site.register(Contact)
admin.site.register(About)
admin.site.register(Sale, SaleModelAdmin)
admin.site.register(Service)