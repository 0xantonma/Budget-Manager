from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('categories', views.categories, name='categories'),
    path('add_category', views.add_category, name='add_category'),
    path('settings', views.settings, name='settings'),
    path('delete_category/<id>', views.delete_category, name='delete'),
    path('delete_subCategory/<id>', views.delete_subCategory, name='delete_subCategory'),
    path('expenses/', views.expenses, name='expenses'),
    path('expenses/delete/<id>', views.deleteExpense, name='expenseDelete'),
    path('expenses/add', views.addExpense, name='addExpense')
]