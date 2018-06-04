from django.db import models


class Campus(models.Model):
    CAMPI = (
        ('Darcy Ribeiro', 'Darcy Ribeiro'),
        ('Gama', 'Faculdade do Gama'),
        ('Planaltina', 'Faculdade UnB Planaltina'),
        ('Ceilândia', 'Faculdade de Ceilândia'),
    )

    name = models.CharField(max_length=50, choices = CAMPI)

    def __str__(self):
        return str(self.name)
