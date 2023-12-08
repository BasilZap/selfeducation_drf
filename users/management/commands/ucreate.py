from users.models import User
from django.core.management import BaseCommand


class Command(BaseCommand):

    def handle(self, *args, **options):
        """
        Команда создания суперпользователя
        """
        user = User.objects.get_or_create(
            email='admin@adminov.ru',
            first_name='admin',
            last_name='Superuser',
            is_staff=True,
            is_superuser=True,
            is_active=True
        )
        # Если пользователь создался - задаем ему пароль
        if user[1]:
            new_user = user[0]
            new_user.set_password('123')
            new_user.save()
        # Если пользователь существует - сообщаем об этом в консоль
        else:
            print('Пользователь существует')
