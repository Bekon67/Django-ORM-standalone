import os

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()

from datacenter.models import Passcard  # noqa: E402

if __name__ == '__main__':
    # Программируем здесь
    print('Количество пропусков:', Passcard.objects.count())  # noqa: T001

    passcards = Passcard.objects.all()
    print(passcards)

    passcard = passcards[0]
    print(f'owner_name: {passcard.owner_name}')
    print(f'owner_name: {passcard.passcode}')
    print(f'owner_name: {passcard.created_at}')
    print(f'owner_name: {passcard.is_active}')

    print(f'Активных пропусков {Passcard.objects.filter(is_active=True).count()}')


