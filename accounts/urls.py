from django.urls import path
from .views import *

app_name = "accounts"

urlpatterns = [
    # employee
    
    path('empregistration/',E_sign_up,name='empregistration'),
    path('E_verification_mail_sent_fun/',E_verification_mail_sent_fun,name='E_verification_mail_sent_fun'),
    path('E_verify_email_fun/',E_verify_email_fun,name="E_verify_email_fun"),
    path('E_set/',E_set_password,name="E_set_password"),
    path('E_forgot/',E_forgot_password,name="E_forgot_password"),
    path('E_otp_verify/',E_otp_verify,name="E_otp_verify"),
    path('E_reset_password/',E_reset_password,name="E_reset_password"),
    path('E_login/',E_log_in,name="E_login"),
    path('eprofile/',E_profile,name="E_profile"),
    path('E_logout/',E_log_out,name="E_logout"),
    
    
    # user
    
    path('uprofile/',U_profile,name='U_profile'),
    path('uregistration/',U_sign_up,name='uregistration'),
    path('U_verification_mail_sent_fun/',U_verification_mail_sent_fun,name='U_verification_mail_sent_fun'),
    path('U_verify_email_fun/',U_verify_email_fun,name="U_verify_email_fun"),
    path('U_set/',U_set_password,name="U_set_password"),
    path('U_forgot/',U_forgot_password,name="U_forgot_password"),
    path('U_otp_verify/',U_otp_verify,name="U_otp_verify"),
    path('U_reset_password/',U_reset_password,name="U_reset_password"),
    path('U_login/',U_log_in,name="U_login"),
    path('U_logout/',U_log_out,name="U_logout")
    
]



