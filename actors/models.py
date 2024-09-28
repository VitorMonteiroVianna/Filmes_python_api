from django.db import models


"""
Aqui deve adicionar as possiveis nacionalidade no formato 'ABREVIAÇÃO', 'NOME COMPLETO'.
"""
NATIONALITY_CHOICES = (
    ('BRA', 'BRASIL'),
    ('USA', 'ESTADOS UNIDOS'),
    ('JPN', 'JAPAO')
)

class Actor(models.Model):
    name = models.CharField(max_length=100)
    birthdate = models.DateField(blank=True, null=True)
    nationality = models.CharField(
        max_length=3,
        choices=NATIONALITY_CHOICES,
        blank=True,
        null=True
    )