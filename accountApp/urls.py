from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

app_name = 'accountApp'

urlpatterns = [
    # 로그인/회원가입
    path('login/', views.JWTLoginView.as_view()),
    path('signup/', views.JWTSignupView.as_view()),

    # 토큰
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
