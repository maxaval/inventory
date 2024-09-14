from django.contrib.auth.models import AbstractUser
from django.db import models
from apps.configuracion.models import Sucursale

# Create your models here.
class UserProfile(AbstractUser):
    # Campos adicionales según tus necesidades
    CONFIA = 'CONFIA'
    CRECER = 'CRECER'
    NOMBRE_AFP_CHOICES = (
		(CONFIA, 'CONFIA'),
		(CRECER, 'CRECER')
	)
    MAMA = 'MAMA'
    PAPA = 'PAPA'
    HERMANO = 'HERMANO'
    HERMANA = 'HERMANA'
    ESPOSA = 'ESPOSA'
    ESPOSO = 'ESPOSO'
    HIJO = 'HIJO'
    HIJA = 'HIJA'
    ABUELA = 'ABUELA'
    ABUELO = 'ABUELO'
    TIO = 'TIO'
    TIA = 'TIA'
    AMIGO = 'AMIGO'
    VECINO = 'VECINO'
    PARENTEZCO_CHOICES = (
		(MAMA, 'MAMA'),
		(PAPA, 'PAPA'),
        (HERMANO, 'HERMANO'),
		(HERMANA, 'HERMANA'),
        (ESPOSA, 'ESPOSA'),
        (ESPOSO, 'ESPOSO'),
        (HIJO, 'HIJO'),
        (HIJA, 'HIJA'),
        (ABUELA, 'ABUELA'),
        (ABUELO, 'ABUELO'),
        (TIO, 'TIO'),
        (TIA, 'TIA'),
        (AMIGO, 'AMIGO'),
        (VECINO, 'VECINO')
	)
    PRIMERCICLO = 'PRIMER CICLO'
    SEGUNDOCICLO = 'SEGUNDO CICLO'
    TERCERCICLO = 'TERCER CICLO'
    BACHILLERATO = 'BACHILLERATO'
    TECNICO = 'TECNICO'
    UNIVERSITARIO = 'UNIVERSITARIO'
    ESTUDIOS_CHOICES = (
        (PRIMERCICLO, 'PRIMER CICLO'),
        (SEGUNDOCICLO, 'SEGUNDO CICLO'),
        (TERCERCICLO, 'TERCER CICLO'),
        (BACHILLERATO, 'BACHILLERATO'),
        (TECNICO, 'TECNICO'),
        (UNIVERSITARIO, 'UNIVERSITARIO'),
    )

    dui = models.CharField(null=True, blank=True, max_length=10)
    nit = models.CharField(null=True, blank=True, max_length=20)
    nomafp = models.CharField(null=True, blank=True, max_length=20, choices = NOMBRE_AFP_CHOICES)
    numafp = models.CharField(null=True, blank=True, max_length=20)    
    isss = models.CharField(null=True, blank=True, max_length=20)
    antecedente = models.BooleanField(null=True, blank=True, default=False)
    solvencia = models.BooleanField(null=True, blank=True)
    vacunaCOVID = models.BooleanField(null=True, blank=True)    
    nombrebanco = models.CharField(null=True, blank=True, max_length=100)
    cuentabanco = models.CharField(null=True, blank=True, max_length=100)
    instituciondisc = models.CharField(null=True, blank=True, max_length=75)
    discapacidad = models.BooleanField(null=True, blank=True)
    direccion = models.CharField(null=True, blank=True, max_length=150)
    telefono = models.CharField(null=True, blank=True, max_length=12)
    celular = models.CharField(null=True, blank=True, max_length=12)
    nomemergencia = models.CharField(null=True, blank=True, max_length=100)
    parenemergencia = models.CharField(null=True, blank=True, max_length=10, choices = PARENTEZCO_CHOICES)
    telemergencia = models.CharField(null=True, blank=True, max_length=12)
    estudios = models.CharField(null=True, blank=True, max_length=20, choices = ESTUDIOS_CHOICES)
    curriculum = models.FileField(upload_to='curriculums', null=True, blank=True)
    email = models.EmailField(null=True, blank=True, max_length=50)
    cargo = models.CharField(null=True, blank=True, max_length=50)
    sexo = models.CharField(null=True, blank=True, max_length=10)
    fecha_in =  models.DateField(null=True, blank=True)
    fecha_exp = models.DateField(null=True, blank=True)
    foto = models.ImageField(upload_to='empleados', null = True, blank=True)
    salario = models.DecimalField(null=True, blank=True, max_digits=6, decimal_places=2)
    viaticos = models.DecimalField(null=True, blank=True, max_digits=6, decimal_places=2)
    cafeteria = models.DecimalField(null=True, blank=True, max_digits=6, decimal_places=2)
    comision = models.DecimalField(null=True, blank=True, max_digits=6, decimal_places=2)
    wallet = models.BooleanField(null=True, blank=True)
    sucursal = models.ForeignKey(Sucursale, on_delete=models.SET_NULL, null=True, blank=True)
    createdate = models.DateTimeField(null=True, blank=True, auto_now_add=True)
    lastupdate = models.DateTimeField(null=True, blank=True, auto_now=True)
    
    def __str__(self):
        return str(self.first_name)
