from django.urls import path, include, re_path
from users import views as user_views
from django.contrib import admin 
from django.urls import path, re_path 
from django.contrib.auth import views as auth_views
import notifications.urls
from django.conf.urls import url

from users.views import (
    login_view,
    logout_view,
    register,
    profile_update,
    healthydeclare_update,
    changepasswd_view,
)
from Home.views import*

from doctor.views import (
    PatientHome,
    PatientHospital,
    PatientOK,
    add_patient,
    patient_update,
    trieuchung_update,
    medical_update,
    delete_patient_home,
    delete_patient_hospital,
    delete_patient_ok,
    
)

from patient.views import(
    tc_update,
    medical_view,
    patient_update2
)

from django.conf import settings
from django.conf.urls.static import static
from forum.views import *

urlpatterns = [
    path('', home_view, name="start"),
    path('home/', homePage, name="home"),
    path('admin/', admin.site.urls),
    path('login/', login_view, name="login"),
    path('logout/', logout_view, name="logout"),
    path('register/', register, name="register"),
    path('changepasswd/', changepasswd_view, name='changepasswd'),


    path('profile/update', profile_update, name="profile-update"),
    path('healthdeclare/update', healthydeclare_update, name="healthdeclare-update"),

    path('patienthome/', PatientHome.as_view(), name="patienthome"),
    path('patienthospital/', PatientHospital.as_view(), name="patienthospital"),
    path('patientok/', PatientOK.as_view(), name="patientok"),
    path('addpatient/', add_patient, name="addpatient"),

    path('patient/<int:patient_id>/', patient_update, name='patient'),
    path('patient/<int:patient_id>/tc/', trieuchung_update, name='patienttc'),
    path('patient/<int:patient_id>/medical/', medical_update, name='medical'),
    path('patient/<int:patient_id>/deletehome/', delete_patient_home, name="deletehome"),
    path('patient/<int:patient_id>/deletehospital/', delete_patient_hospital, name="deletehospital"),
    path('patient/<int:patient_id>/deleteok/', delete_patient_ok, name="deleteok"),

    path('tcupdate/', tc_update, name="tc-update"),
    path('medical/', medical_view, name="medical-view"),
    path('update/', patient_update2, name="patient-update"),

    path('forum/', TopicListView.as_view(), name="forum-index"),
    path('forum/topic/add/', TopicCreateView.as_view(), name='topic-add'),
    path('forum/topic/<int:pk>/', TopicDetailView.as_view(), name='topic-detail'),
    path('topic/<int:pk>/newpost/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    url('^inbox/notifications/', include(notifications.urls, namespace='notifications')),



    path('reset_password/',auth_views.PasswordResetView.as_view(template_name="users/password_reset.html"),name="reset_password"),
    path('reset_password_sent/',auth_views.PasswordResetDoneView.as_view(template_name="users/password_reset_sent.html"),name="password_reset_done"),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name="users/password_reset_form.html"), name="password_reset_confirm"),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="users/password_reset_done.html"),name="password_reset_complete"),
 
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

