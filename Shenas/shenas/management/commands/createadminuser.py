from getpass import getpass

from django.contrib.auth import get_user_model
from django.core.management import BaseCommand

from shenas.models import UserRole

User = get_user_model()


class Command(BaseCommand):

    def handle(self, *args, **options):
        username = input('Username: ')
        password = getpass('password: ')
        User.objects.create_user(username=username, password=password, role=UserRole.ADMIN)
