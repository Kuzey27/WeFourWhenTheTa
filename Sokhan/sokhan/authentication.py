from django.contrib.auth import get_user_model
from rest_framework.authentication import BaseAuthentication

User = get_user_model()


class ShenasAuthentication(BaseAuthentication):
    def authenticate(self, request):
        print(request.headers)
        username = request.headers.get('x-username', None)
        if username is None:
            return None
        return User.objects.get_or_create(username=username)[0], None


