from django.urls import path
from .import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from task1 import settings

urlpatterns = [
    
    path('',views.login_page,name='login_page'),
    path('register_user',views.register_user,name='register_user'),
    path('login_user',views.login_user,name='login_user'),
    path('doctor_dashboard',views.doctor_dashboard,name='doctor_dashboard'),
    path('patient_dashboard',views.patient_dashboard,name='patient_dashboard'),
    path('logout_user',views.logout_user,name='logout_user'),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
if settings.DEBUG:  # only for development
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)