from django.db import models
from django.contrib.auth.models import User
import datetime

class Clients(models.Model):
    nom = models.CharField(max_length=255)
    prenom = models.CharField(max_length=255)
    naissance = models.DateField(blank=True, null=True)
    sexe = models.CharField(max_length=2)
    telephone = models.CharField(max_length=255)
    date_rdv = models.DateField(blank=True, null=True)
    heure_rdv = models.TimeField(blank=True, null=True)
    date_contact = models.DateField(blank=True, null=True)
    heure_contact = models.TimeField(blank=True, null=True)
    motif = models.TextField(null=True)
    comment = models.TextField(blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    @property
    def age(self):
        if self.naissance:
            return int((datetime.datetime.now().date() - self.naissance).days / 365.25)
        else:
            return '-'