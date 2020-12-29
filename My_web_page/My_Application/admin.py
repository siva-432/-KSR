from django.contrib import admin
from My_Application.models import About,Contact,Cource,Python,Django,Datascience,Bigdata,Html_css
# Register your models here.
class AboutAdmin(admin.ModelAdmin):
    list_display = ['name','text']
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name','text1','mail','mobile']

class CourceAdmin(admin.ModelAdmin):
    list_display = ['name','image1','image2','image3','image4','image5','text1']

class PythonAdmin(admin.ModelAdmin):
    list_display = ['pname','text2']

class DjangoAdmin(admin.ModelAdmin):
    list_display = ['dname','text3']

class DatascienceAdmin(admin.ModelAdmin):
    list_display = ['Dname','text4']

class BigadataAdmin(admin.ModelAdmin):
    list_display = ['Bname','text5']

class Html_cssAdmin(admin.ModelAdmin):
    list_display = ['Hname','text6']
admin.site.register(About)
admin.site.register(Contact)
admin.site.register(Cource)
admin.site.register(Python)
admin.site.register(Django)
admin.site.register(Datascience)
admin.site.register(Bigdata)
admin.site.register(Html_css)


