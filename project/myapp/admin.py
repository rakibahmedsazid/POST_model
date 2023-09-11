from django.contrib import admin
from myapp. models import Office

# Register your models here.

class OfficeAdmin(admin.ModelAdmin):
    list_display=('name','department')
    search_fields=('name','department')
    list_filter=('name','department')



admin.site. register(Office,OfficeAdmin)
