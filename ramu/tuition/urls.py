from django.contrib import admin
from django.urls import include,path
from django.contrib.auth import views as auth_views

from . import views
app_name = "tuition"

urlpatterns = [
    path("",views.index, name="index"),
    path("curriculum",views.curriculum, name="curriculum"),
    path("methodology",views.methodology, name="methodology"),
    path("about",views.about, name="about"),
    path("mission",views.mission, name="mission"),
    path("feedback",views.feedback, name="feedback"),
    path("enquiry",views.enquiry, name="enquiry"),
    # path("login",views.login_view, name="login"),
    # path('login/', auth_views.login, {'template_name': 'login.html'}, name='login'),
    path("login_view", views.login_view, name="login_view"),
    #path("logout",views.logout, name="logout"),
    path("post_feedback",views.post_feedback, name="post_feedback"),
    path("post_enquiry",views.post_enquiry, name="post_enquiry"),
    path('sign_up/',views.sign_up,name="sign_up"),
]
