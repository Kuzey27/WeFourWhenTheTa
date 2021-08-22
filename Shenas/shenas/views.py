from django.contrib.auth.models import update_last_login
from rest_framework.generics import CreateAPIView, RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_401_UNAUTHORIZED, HTTP_200_OK
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication, JWTTokenUserAuthentication
from rest_framework_simplejwt.settings import api_settings
from rest_framework_simplejwt.tokens import RefreshToken

from shenas.serializers import UserSignUpSerializer, ProfileSerializer


class SingUpView(CreateAPIView):
    def create(self, request, *args, **kwargs):
        signup_serializer = UserSignUpSerializer(data=request.data)
        signup_serializer.is_valid(raise_exception=True)
        user = signup_serializer.save()
        refresh = RefreshToken.for_user(user)

        if api_settings.UPDATE_LAST_LOGIN:
            update_last_login(None, user)

        return Response(
            data={
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            },
            status=HTTP_201_CREATED
        )


class AuthorizeView(APIView):
    authentication_classes = [JWTAuthentication]

    def get(self, request):
        if request.user.is_anonymous:
            return Response(status=HTTP_200_OK)
        return Response(
            headers={
                'x-username': request.user.username,
                'x-userrole': request.user.role,
            },
            status=HTTP_200_OK,
        )


class RetrieveUpdateProfileAPIView(RetrieveUpdateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = ProfileSerializer

    def get_object(self):
        return self.request.user