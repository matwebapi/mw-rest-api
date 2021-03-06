from django.core.management.base import BaseCommand, CommandError

from api.models import *


class Command(BaseCommand):
    help = 'Populate some initial models data for development purposes.'

    def handle(self, *args, **options):
        print('Creating CAMPI\n\n')
        gama = Campus.objects.get_or_create(name='Gama')[0]
        darcy = Campus.objects.get_or_create(name='Darcy Ribeiro')[0]
        planaltina = Campus.objects.get_or_create(name='Planaltina')[0]
        ceilandia = Campus.objects.get_or_create(name='Ceilândia')[0]

        print('Creating DEPARTAMENT\n\n')
        fga = Department.objects.get_or_create(code=650, initials='FGA',
                name='UnB - Faculdade do Gama', campus=gama)[0]

        code = models.IntegerField(primary_key=True)
        name = models.CharField(max_length=50)
        initials = models.CharField(max_length=256)
        campus = models.ForeignKey(Campus, on_delete=models.CASCADE)

        print('Creating SUBJECTS\n\n')
        asa = Subject.objects.get_or_create(code=104779,
                            name='AERODINAMICA DE SISTEMAS AEROESPACIAIS',
                            department=fga)[0]

        print('Creating Courses\n\n')
        PRESENCIAL = 'P'
        DIURNO = 'D'
        software = Course.objects.get_or_create(code=1635, name='ENGENHARIA DE SOFTWARE', genre=PRESENCIAL,
                          shift=DIURNO, campus=gama)[0]

        eletronica = Course.objects.get_or_create(code=1601, name='ENGENHARIA ELETRÔNICA', genre=PRESENCIAL,
                          shift=DIURNO, campus=gama)[0]


