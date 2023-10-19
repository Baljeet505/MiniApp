from django.urls import path
from Project import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.signin,name='signin'),
    path('signup',views.signup,name='signup'),
    path('userhome',views.userhome,name='userhome'),
    path('logout',views.logoutUser, name='logout'),
    # creating paths for opening views related to password reset
    path('password_reset' , auth_views.PasswordResetView.as_view(template_name="Project/password_reset.html"), name="password_reset"),    
    path('password_reset_done' , auth_views.PasswordResetDoneView.as_view(template_name="Project/password_reset_done.html"), name="password_reset_done"),

    path('password_reset_confirm/<uidb64>/<token>/' , auth_views.PasswordResetConfirmView.as_view(template_name="Project/password_reset_confirm.html"), name="password_reset_confirm"),
    path('password_reset_complete' , auth_views.PasswordResetCompleteView.as_view(template_name="Project/password_reset_complete.html"), name="password_reset_complete")
]