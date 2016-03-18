from django.contrib import admin
from .models import JfClients, JfGender, JfSizes, JfTrainers, JfTrainings

admin.site.register(JfClients)
admin.site.register(JfGender)
admin.site.register(JfSizes)
admin.site.register(JfTrainers)
admin.site.register(JfTrainings)