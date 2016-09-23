from django.contrib import admin
from main.models import Home, Contact, Menu, Uslugi, Submenu, Mainmenu, Sale, Onas, Problem, Product

# Register your models here.
class ProductModelAdmin(admin.ModelAdmin):
	list_display = ["title", "price", "archive", "description", "category"]
	list_filter = ["category", "archive"]
	search_fields = ["title", "description", "text"]
	list_editable = ["price", "archive"]
	class Meta:
		model = Product

admin.site.register(Home)
admin.site.register(Contact)
admin.site.register(Menu)
admin.site.register(Uslugi)
admin.site.register(Submenu)
admin.site.register(Mainmenu)
admin.site.register(Sale)
admin.site.register(Onas)
admin.site.register(Problem)
admin.site.register(Product, ProductModelAdmin)