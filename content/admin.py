from django.contrib import admin
from .models import Project, Technology
# Register your models here.


admin.site.regitser(Project)
admin.site.register(Technology)
