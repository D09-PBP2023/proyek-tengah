from django.contrib import admin
from book_request.models import RequestBook

class BookRequestAdmin(admin.ModelAdmin):
    list_display = ['name', 'request_status']
    
admin.site.register(RequestBook)