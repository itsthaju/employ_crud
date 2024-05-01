from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('list/', views.employee_list, name='employee_list'),
    path('', views.employee_login, name='employee_login'),
    path('logout/', views.logout_view, name='logout'),
    path('add/', views.employee_create, name='employee_create'),
    path('<int:employee_id>/delete/', views.employee_delete, name='employee_delete'),
    path('<int:employee_id>/', views.employee_detail, name='employee_detail'),
    path('<int:employee_id>/', views.employee_profile_update, name='employee_profile_update'),
    path('<int:employee_id>/update/', views.employee_update, name='employee_update'),
    path('dashboard/', views.employee_dashboard, name='employee_dashboard'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
