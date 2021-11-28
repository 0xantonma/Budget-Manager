from django.contrib import admin
from .models import Expenses, Categories, SubCategories
# Register your models here.
admin.site.register(Expenses)
admin.site.register(Categories)
admin.site.register(SubCategories)