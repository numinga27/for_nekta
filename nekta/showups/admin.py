from django.contrib import admin

# Register your models here.
from .models import Request, RequestMessage


class RequestAdmin(admin.ModelAdmin):
    list_display = ('pk', 'description', 'date', 'status')
    search_fields = ('description',)
    list_filter = ('date',)
    empty_value_display = '-пусто-'


admin.site.register(Request, RequestAdmin)
admin.site.register(RequestMessage)