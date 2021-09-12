from django.urls import path
from blog import views

urlpatterns = [

    path('', views.Login, name="Login"),
    path('index/', views.Index, name="Index"),
    path('mobile-table/', views.MobilePhone, name="MobilePhone"),
    path('inbox-table/', views.InboxTable, name="InboxTable"),
    path('change-password/', views.ChangePassword, name="ChangePassword"),
    path('send-sms/', views.SendSms, name="SendSms"),
    path('change-link/', views.ChangeLink, name="ChangeLink"),
    

]
