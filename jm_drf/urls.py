from allauth.account.views import confirm_email
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from accountApp import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('accounts/', include('dj_rest_auth.urls')),
    path('accounts/', include('dj_rest_auth.registration.urls')),
    path('accounts/', include('accountApp.urls')),
    path('accounts/', include('allauth.urls')), # 이거 빼야 하나?
    path('accounts-rest/registration/account-confirm-email/(?P<key>.+)/$', confirm_email, name='account_confirm_email'),

    # 로그인/회원가입
    # path('login/', views.JWTLoginView.as_view()),
    # path('signup/', views.JWTSignupView.as_view()),

    # 토큰
    # path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
