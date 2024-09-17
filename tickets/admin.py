from django.contrib import admin
from .models import Ticket, Sample

# Register your models here.

admin.site.register(Ticket)
admin.site.register(Sample)