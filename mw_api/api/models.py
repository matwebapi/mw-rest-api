from django.db import models


class Campus(models.Model):
    CAMPI = (
        ('DARCY', 'Darcy Ribeiro'),
        ('FGA', 'Faculdade do Gama'),
        ('FUP', 'Faculdade UnB Planaltina'),
        ('FCE', 'Faculdade de Ceilândia'),
    )

    name = models.CharField(max_length=50, choices=CAMPI)

    def __str__(self):
        return str(self.name)


class Department(models.Model):
    code = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    initials = models.CharField(max_length=256)
    campus = models.ForeignKey(Campus, on_delete = models.CASCADE, blank=True,
    null=True)


class Subject(models.Model):
    code = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    department = models.ForeignKey(Department, on_delete = models.CASCADE,
    blank=True, null=True)

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
