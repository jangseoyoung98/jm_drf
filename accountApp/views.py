from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from accountApp.serializers import JWTSignupSerializer, JWTLoginSerializer


class JWTSignupView(APIView):
    serializer_class = JWTSignupSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid(raise_exception=False):
            user = serializer.save(request)

            token = RefreshToken.for_user(user)
            refresh = str(token)
            access = str(token.access_token)

            return JsonResponse({'user': user,
                                 'access': access,
                                 'refresh' : refresh})
        else:
            return


class JWTLoginView(APIView):
    serializer_class = JWTLoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid(raise_exception=False):
            user = serializer.validated_data['user']
            access = serializer.validated_data['access']
            refresh = serializer.validated_data['refresh']

            return JsonResponse({
                'user': user,
                'access': access,
                'refresh': refresh})
        else:
            return


