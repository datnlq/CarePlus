from django.urls import path, include, re_path
from users import views as user_views
from django.contrib import admin 
from django.urls import path, re_path 


from users.views import (
    login_view,
    logout_view,
    register,
    profile_update,
    healthydeclare_update
)
from Home.views import(
    home_view
)

from doctor.views import (
    PatientHome,
    PatientHospital,
    PatientOK,
    add_patient,
    patient_update,
    trieuchung_update,
    medical_update
)

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', home_view, name="home"),
    path('admin/', admin.site.urls),
    path('login/', login_view, name="login"),
    path('logout/', logout_view, name="logout"),
    path('register/', register, name="register"),

    path('profile/update', profile_update, name="profile-update"),
    path('healthdeclare/update', healthydeclare_update, name="healthdeclare-update"),

    path('patienthome/', PatientHome.as_view(), name="patienthome"),
    path('patienthospital/', PatientHospital.as_view(), name="patienthospital"),
    path('patientok/', PatientOK.as_view(), name="patientok"),
    path('addpatient/', add_patient, name="addpatient"),

    path('patient/<int:patient_id>/', patient_update, name='patient'),
    path('patient/<int:patient_id>/tc/', trieuchung_update, name='patienttc'),
    path('patient/<int:patient_id>/medical/', medical_update, name='medical'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

