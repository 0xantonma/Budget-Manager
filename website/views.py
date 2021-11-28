from typing import Set
from django.shortcuts import render, redirect
from .forms import CategoryForm, ExpenseForm, SettingsForm, SubCategoryForm
from .models import Categories, Expenses, Settings, SubCategories
from datetime import datetime
from django.db.models import Sum
# Create your views here.

def home(request):
    dt = datetime.today()
    monthFormat = dt.strftime("%B %Y")
    categories = Categories.objects.all()
 
    # Top categories by spending 
    categories_top = []
    for category in categories:
        item_top = {
            'amount': Expenses.objects.filter(date__month=dt.month, category=category.id).aggregate(Sum('amount')),
            'name' : category.name,
            'icon' : category.icon
        }
        categories_top.append(item_top)
    # End top categories by spending

    return render(request, 'website/home.html', {
        'expenses': Expenses.objects.filter(date__month=dt.month),
        'categories': categories,
        'month': monthFormat,
        'totalSpent': Expenses.objects.filter(date__month=dt.month).aggregate(Sum('amount')),
        'categories_top': categories_top,
        'currencySymbol': Settings.objects.get(settingName='currency')
    })

def add_category(request):
    if request.method == 'GET':
        category_form = CategoryForm()
        subcategory_form = SubCategoryForm()
    else:
        category_form = CategoryForm(request.POST)
        subcategory_form = SubCategoryForm(request.POST)
        if category_form.is_valid():
            category_form.save()

        if subcategory_form.is_valid():
            subcategory_form.save()

    return render(request, 'website/add_category.html', {
        'form': category_form,
        'form2': subcategory_form,
        'parentCategories': Categories.objects.all()
        })

def categories(request):
    return render(request, 'website/categories.html', {
        'categories': Categories.objects.all(),
        'subCategories': SubCategories.objects.all(),
        })

def delete_category(request, id):
    Categories.objects.get(pk=id).delete()
    return redirect('categories')

def delete_subCategory(request, id):
    SubCategories.objects.get(pk=id).delete()
    return redirect('categories')


def expenses(request):
    return render(request, 'website/expenses.html', {
        'expenses': Expenses.objects.all(),
        'currencySymbol': Settings.objects.get(settingName='currency')
    })

def deleteExpense(request, id):
    Expenses.objects.get(pk=id).delete()
    return redirect('expenses')

def addExpense(request):
    if request.method == 'GET':
        expense_form = ExpenseForm()
    else:
        expense_form = ExpenseForm(request.POST)
        if expense_form.is_valid():
            expense_form.save()
            return redirect('expenses')


    # Sort categories for work
    mainCategories = Categories.objects.all()
    displayCategories = {}

    for item in mainCategories:
        displayCategories[item.name] = {
            'list': SubCategories.objects.filter(category=item.id)
        }

    # END sorting categories

    return render(request, 'website/addExpense.html', {
        'form': expense_form,
        'categories': displayCategories,
        'time': datetime.now().strftime("%Y-%m-%d"),
        'currencySymbol': Settings.objects.get(settingName='currency')
    })

def settings(request):
    if request.method == 'GET':
        settings_form = SettingsForm()
    else:
        settings_form = SettingsForm(request.POST)
        if settings_form.is_valid():
            
            if settings_form.cleaned_data['settingName'] == 'currency':
                Settings.objects.filter(settingName='currency').update(settingValue=settings_form.cleaned_data['settingValue'])

                
    return render(request, 'website/settings.html', {
        'currencySymbol': Settings.objects.get(settingName='currency')
    })