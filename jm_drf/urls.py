from allauth.account.views import confirm_email
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from accountApp import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('users/', include('dj_rest_auth.urls')),
    path('users/', include('dj_rest_auth.registration.urls')),
    path('users/', include('accountApp.urls')),
    path('users/', include('allauth.urls')), # 이거 빼야 하나?
    path('users-rest/registration/account-confirm-email/(?P<key>.+)/$', confirm_email, name='account_confirm_email'),

]
