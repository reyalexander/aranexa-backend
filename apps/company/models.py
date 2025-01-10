from django.db import models
from apps.user.models import Account
from django.contrib.postgres.fields import ArrayField

class CompanyInformation(models.Model):
    NEED_STAFF_CHOICES = (
        (1, "Sí, es necesario"),
        (2, "No, puedo manejarlo internamente"),
        (3, "No, pero lo haré"),
    )

    KNOWLEDGE_CHOICES = (
        (1, "1"),
        (2, "2"),
        (3, "3"),
        (4, "4"),
        (5, "5"),
        (6, "No Aplica"),
    )
    
    account_id = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True, verbose_name="Usuario")
    year_foundation = models.TextField(
        max_length=100, null=True, blank=True, 
        verbose_name="Año de fundacion"
    )
    market = ArrayField(
        models.TextField(),
        size=20,
        null=True,
        blank=True, 
        verbose_name="Mi Mercado es:"
    )
    peru_was_founded = models.BooleanField(default=True, null=False, verbose_name="Se fundo en Peru:")
    country_was_founded = models.TextField(max_length=100, null=True, blank=True, verbose_name="En qué país se fundó")
    people_joined = models.IntegerField(
        null=True, blank=True, 
        verbose_name="Qué número de personas se asociaron para su creación"
    )
    need_hire_staff = models.PositiveSmallIntegerField(
        choices=NEED_STAFF_CHOICES, null=True, blank=True, 
        verbose_name="¿Actualmente necesito contratar personal adicional para que mi empresa/emprendimiento pueda funcionar?"
    )
    payment_vouchers = ArrayField(
        models.TextField(),
        size=20,
        null=True,
        blank=True,
        verbose_name="Emito comprobantes de pago"
    )
    main_challenges = ArrayField(
        models.TextField(),
        size=20,
        null=True,
        blank=True,
        verbose_name="Cuáles son los principales retos que enfrenta mi negocio"
    )
    political = models.PositiveSmallIntegerField(
        choices=KNOWLEDGE_CHOICES, null=True, blank=True, verbose_name="Político"
    )
    social = models.PositiveSmallIntegerField(
        choices=KNOWLEDGE_CHOICES, null=True, blank=True, verbose_name="Social"
    )
    economic = models.PositiveSmallIntegerField(
        choices=KNOWLEDGE_CHOICES, null=True, blank=True, verbose_name="Económico"
    )
    technological = models.PositiveSmallIntegerField(
        choices=KNOWLEDGE_CHOICES, null=True, blank=True, verbose_name="Tecnológico"
    )
    environmental = models.PositiveSmallIntegerField(
        choices=KNOWLEDGE_CHOICES, null=True, blank=True, verbose_name="Ambiental"
    )
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización")



class CompanyBrand(models.Model):
    BRAND_NAME_REGISTERED_CHOICES = (
        (1, "Sí"),
        (2, "No"),
        (3, "Prefiero no decirlo"),
    )

    account_id = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True, verbose_name="Usuario")
    brand_information = models.CharField(max_length=100, null=True, blank=True, verbose_name="Datos de mi marca")
    brand_name_registered = models.PositiveSmallIntegerField(
        choices=BRAND_NAME_REGISTERED_CHOICES, null=True, blank=True, 
        verbose_name="El nombre de mi marca está registrada legalmente"
    )
    currently_present_media = ArrayField(
        models.TextField(),
        size=10,
        null=True,
        blank=True,
        verbose_name="Actualmente tengo presencia en los siguientes medios",
    )
    goals_achieve = ArrayField(
        models.TextField(),
        size=10,
        null=True,
        blank=True,
        verbose_name="Mis metas a conseguir son",
    )
    digital_media = models.IntegerField(
        blank=True, 
        null=True, 
        verbose_name="¿Los medios digitales/físicos en los que tengo presencia me están ayudando a conseguir mis metas?"
    )

    def __str__(self):
        return self.brand_information or f"CompanyBrandInfo #{self.id}"
