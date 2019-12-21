from django.core.exceptions import ValidationError
import datetime


def validate_rdv(value):
    rdv = value
    if rdv is None:
        raise ValidationError("Veuillez rentrer une date valide")

    return datetime.datetime.strptime(rdv.replace('T', ' '), '%Y-%m-%d %H:%M')