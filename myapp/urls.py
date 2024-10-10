from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views 

urlpatterns = [
    path('', views.index),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('service/',views.service,name='service'),
    path('details/', views.details, name='details'),
    path('update/', views.update, name='update'),
    path('add_employee', views.add_employee, name='add_employee'),  # Add this line
    path('delete_employee/<int:id>/', views.delete_employee, name='delete_employee'),
    path('update_employee/<int:id>/', views.update_employee, name='update_employee'),  # Correct path for update
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)   