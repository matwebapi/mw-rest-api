from django.db import models


class Campus(models.Model):
    CAMPI = (
        ('Darcy Ribeiro', 'Darcy Ribeiro'),
        ('Gama', 'Faculdade do Gama'),
        ('Planaltina', 'Faculdade UnB Planaltina'),
        ('Ceilândia', 'Faculdade de Ceilândia'),
    )

    name = models.CharField(max_length=50, choices=CAMPI)

    def __str__(self):
        return str(self.name)


class Course(models.Model):
    GENRE = (
             ('D', 'Distância'),
             ('P', 'Presencial'),
            )

    SHIFTS = (
              ('D', 'Diurno'),
              ('N', 'Noturno'),
             )

    code = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=256)
    genre = models.CharField(max_length=50, choices=GENRE)
    shift = models.CharField(max_length=50, choices=SHIFTS)
    campus = models.ForeignKey(Campus, on_delete = models.CASCADE)
