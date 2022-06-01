import clearbit
from django.conf import settings
from pyhunter import PyHunter


def get_more_info(email):
    clearbit.key = settings.CLEARBIT_KEY
    return clearbit.Person.find(email=email, stream=True)


def verify_email(email):
    hunter = PyHunter(settings.HUNTER_KEY)
    return hunter.email_verifier(email)
