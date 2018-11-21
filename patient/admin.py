from django.contrib import admin
# Register your models here.
from .models import Patient
class PatientAdmin(admin.ModelAdmin):
    
    list_distplay = ('name','nick_name','gender','dob','telephone')
    
admin.site.register(Patient,PatientAdmin)