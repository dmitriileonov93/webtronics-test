from django.conf import settings

import clearbit
from pyhunter import PyHunter


def get_more_info(email):
    clearbit.key = settings.CLEARBIT_KEY
    response = clearbit.Person.find(email=email, stream=True)
    return response


def verify_email(email):
    hunter = PyHunter(settings.HUNTER_KEY)
    result = hunter.email_verifier(email)
    return result
