from django import forms
from django.db.models.base import Model
from django.forms import ModelForm
from .models import Categories, Expenses, Settings, SubCategories
from django import forms


class CategoryForm(ModelForm):
    class Meta:
        model = Categories
        fields = ['name', 'icon']

class SubCategoryForm(ModelForm):
    class Meta:
        model = SubCategories
        fields = ['name', 'category']


class ExpenseForm(ModelForm):
    class Meta:
        model = Expenses
        fields = ['amount', 'note', 'date', 'category']

class SettingsForm(forms.Form):
    settingName = forms.CharField()
    settingValue = forms.CharField()
