from django.urls import path
from .views import (avataractualizado, bandeja, borrar, enviados, leerenviados, leermail, profile, list_user, redactar, redactarmail,profileactualizado, borrarusuario)
from django.contrib.auth.views import PasswordResetView, PasswordResetConfirmView, PasswordResetCompleteView, PasswordResetDoneView


urlpatterns = [
     path('perfil/<id>',profile, name ='perfil'),
     path('list-user/', list_user, name="list-user"),
     path('leer/<id>', leermail, name="leermail"),
     path('leerenviados/<id>', leerenviados, name="leerenviados"),
     path('bandeja/', bandeja, name="bandeja"),
     path('redactar/', redactarmail, name="redactar"),
     path('redactar_usuario/<id>', redactar, name="redactarusuario"),
     path('enviados/', enviados, name="enviados"),
     path('borrar/<id>', borrar, name="borrar"),
     path('avataractualizado/<id>', avataractualizado, name="avataractualizado"),
     path('profileactualizado/<id>', profileactualizado, name="profileactualizado"),
     path('borrarusuario/<id>', borrarusuario, name="borrarusuario"),
     path('recuperar/passwordreset', PasswordResetView.as_view(template_name='recuperar/password_reset_form.html', email_template_name='recuperar/password_reset_email.html'), name='passwordreset'),
     path('recuperar/passwordresetdone', PasswordResetDoneView.as_view(template_name='recuperar/password_reset_done.html'), name='password_reset_done'),
     path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name='recuperar/password_reset_confirm.html'), name='password_reset_confirm'),
     path('recuperar/passwordresetdone', PasswordResetCompleteView.as_view(template_name='recuperar/password_reset_complete.html'), name='password_reset_complete'),
    
]