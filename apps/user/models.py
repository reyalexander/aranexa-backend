from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models
from django.contrib.postgres.fields import ArrayField

class CustomUserManager(UserManager):
    """
    Si necesitas personalizar el UserManager,
    puedes sobreescribir métodos aquí.
    """
    pass

class User(AbstractUser):

    objects = CustomUserManager()

    class Meta:
        verbose_name = "usuario"
        verbose_name_plural = "usuarios"
        ordering = ["first_name"]

    def str(self):
        return self.first_name," ", self.last_name
    
class Account(models.Model):
    GENDER_CHOICES = (
        (1, "Femenino"),
        (2, "Masculino"),
        (3, "No Binario"),
        (4, "Otro"),
        (5, "Prefiero no decirlo"),
    )

    LEVEL_OF_STUDY_CHOICES = (
        (1, "Básica primaria"),
        (2, "Básica secundaria"),
        (3, "Técnica profesional"),
        (4, "Universitaria"),
        (5, "Licenciatura"),
        (6, "Posgrado"),
    )

    ACADEMIC_OR_WORK_AREA_CHOICES = (
        (1, "Administración, negocios y ventas"),
        (2, "Artes y humanidades"),
        (3, "Ingeniería, manufactura y construcción"),
        (4, "Ciencias exactas y naturales"),
        (5, "Ciencias sociales y derecho"),
        (6, "Ciencias de la salud"),
        (7, "Otro"),
    )

    full_name = models.CharField(max_length=50, null=True, blank=True, verbose_name="Nombre Completo")
    year_birthday = models.IntegerField(null=True, blank=True, verbose_name="Año de Nacimiento")
    nationality = models.CharField(max_length=20, blank=True, null=True, verbose_name="Nacionalidad")
    gender = models.PositiveSmallIntegerField(
        choices=GENDER_CHOICES, null=True, blank=True, verbose_name="Genero"
    )
    level_of_study = models.PositiveSmallIntegerField(
        choices=LEVEL_OF_STUDY_CHOICES, null=True, blank=True, verbose_name="Nivel de Estudio"
    )
    academic_or_work_area = ArrayField(
        models.TextField(),
        size=10,
        null=True,
        blank=True,
        verbose_name="En qué área me he desarrollado a nivel académico / laboral",
    )
    current_position = models.CharField(max_length=50, blank=True, null=True, verbose_name="Puesto actual")

    def __str__(self):
        return self.full_name