from django.contrib import admin
from main.models import Home, About, Contact, Service, Article, Social

class TinyMCEAdmin(admin.ModelAdmin):
	class Media:
		js = ('/static/static_root/grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js', '/static/static_root/grappelli/tinymce_setup/tinymce_setup.js',)

admin.site.register(Home, TinyMCEAdmin)

admin.site.register(About, TinyMCEAdmin)

admin.site.register(Contact, TinyMCEAdmin)

admin.site.register(Service, TinyMCEAdmin)

admin.site.register(Article, TinyMCEAdmin)

admin.site.register(Social, TinyMCEAdmin)