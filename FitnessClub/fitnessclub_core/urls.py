from django.urls import path
from . import views

app_name = 'fitnessclub_core'

urlpatterns = [
    path('', views.gym_list, name='gym_list'),
    path('gym/<int:id>/', views.gym_detail, name='gym_detail'),
    path('group_class/', views.group_class_list, name='group_class_list'),
    path('group_class/<int:id>/', views.group_class_detail, name='group_class_detail'),
    path('group_class/create/', views.create_group_class, name='create_group_class'),
    path('group_class/<int:id>/edit/', views.edit_group_class, name='edit_group_class'),
    path('group_class/<int:id>/delete/', views.delete_group_class, name='delete_group_class'),
    path('fclub/', views.fclub, name='fclub'),
    path('about_us/', views.about_us, name='about_us'),
    path('promotions', views.promotions, name='promotions'),
    path('news_list/', views.news_list, name='news_list'),
    path('employees/', views.employee_list, name='employee_list'),
    path('privacy_policy/', views.privacy_policy, name='privacy_policy'),
    path('vacancies/', views.vacancies, name='vacancies'),
    path('faq/', views.faq, name='faq')
]