from . import views
from django.urls import path
app_name = 'credentials'
urlpatterns = [
    path('',views.index,name='index'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('detail/',views.detail,name='detail'),
    path('new/', views.new, name='new'),
    path('logout/', views.logout, name='logout'),
    path('card/',views.card,name='card'),
    path('add/', views.person_create_view, name='person_add'),
    path('<int:pk>/', views.person_update_view, name='person_change'),

    path('ajax/load-cities/', views.load_cities, name='ajax_load_cities'),  # AJAX




]