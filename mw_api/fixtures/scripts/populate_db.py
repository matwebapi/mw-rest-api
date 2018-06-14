from api.models import *

print('Creating CAMPI\n\n')
gama = Campus.objects.get_or_create(name='Gama')[0]
darcy = Campus.objects.get_or_create(name='Darcy Ribeiro')[0]
planaltina = Campus.objects.get_or_create(name='Planaltina')[0]
ceilandia = Campus.objects.get_or_create(name='Ceilândia')[0]

print('Creating Courses\n\n')
PRESENCIAL = 'P'
DIURNO = 'D'
software = Course.objects.get_or_create(code=1635, name='ENGENHARIA DE SOFTWARE', genre=PRESENCIAL,
                  shift=DIURNO, campus=gama)[0]

eletronica = Course.objects.get_or_create(code=1601, name='ENGENHARIA ELETRÔNICA', genre=PRESENCIAL,
                  shift=DIURNO, campus=gama)[0]
