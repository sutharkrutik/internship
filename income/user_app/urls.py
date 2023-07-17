
from django.urls import path

from . import views

urlpatterns = [
    path('login/', views.login,name="login"),
    path('register/', views.register,name="register"),
    path('forgotpass/', views.forgotpass, name="forgotpass"),
    path('newpassOTP/', views.newpassOTP, name="newpassOTP"),
    path('newpass/', views.newpass, name="newpass"),
    path('about/', views.about, name="about"),
    path('contactus/', views.contactus, name="contactus"),
    path('home/', views.home, name="home"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('profile/', views.profile, name="profile"),
    path('reg_edit/', views.reg_edit, name='reg_edit'),
    path('reg_update/', views.reg_update, name='reg_update'),
    path('income/', views.income, name="income"),
    path('expense/', views.expense, name="expense"),
    path('manage_income/', views.manage_income,name="manage_income"),
    path('manage_expense/', views.manage_expense,name= "manage_expense"),
    path('edit_income/<int:id>',views.edit_income , name = 'edit_income'),
    path('update_income/<int:id>', views.update_income, name='update_income'),
    path(r'^delete_income/(?P<pk>[0-9]+)/$', views.delete_income, name='delete_income'),
    path('edit_expense/<int:id>', views.edit_expense, name='edit_expense'),
    path('update_expense/<int:id>', views.update_expense, name='update_expense'),
    path(r'^delete_expense/(?P<pk>[0-9]+)/$', views.delete_expense, name='delete_expense'),
    path('logout/', views.logout, name="logout"),

]


