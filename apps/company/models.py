from django.db import models
from apps.user.models import User
from django.contrib.postgres.fields import ArrayField

class CompanyInformation(models.Model):
    MARKET_CHOICES = (
        (1, "Tecnología y software"),
        (2, "Alimentos y bebidas"),
        (3, "Salud y bienestar"),
        (4, "Mascotas y otros animales"),
        (5, "Educación, consultorías o asesorías"),
        (6, "Gestión, marketing y diseño"),
        (7, "Arte, diseño y artesanía"),
        (8, "Entretenimiento y ocio"),
        (9, "Moda y estilo de vida"),
        (10, "Finanzas y seguros"),
        (11, "Sostenibilidad y medio ambiente"),
        (12, "Transporte, logística y exportación"),
        (13, "Vivienda, hogar y familia"),
        (14, "Deporte y estilo de vida"),
        (15, "Turismo y cultura"),
    )

    NEED_STAFF_CHOICES = (
        (1, "Sí, es necesario"),
        (2, "No, puedo manejarlo internamente"),
        (3, "No, pero lo haré"),
    )

    PAYMENT_CHOICES = (
        (1, "Facturas"),
        (2, "Boletas de venta"),
        (3, "Tickets"),
        (4, "No sé cuál emitir"),
        (5, "No necesito"),
        (6, "Otros"),
    )

    PAYMENT_CHOICES = (
        (1, "Acceso a financiamiento"),
        (2, "Normas fiscales y legales complejas"),
        (3, "Saturación de mercado (mucha competencia)"),
        (4, "Dificultad para adaptarse a nuevos entornos e integrar herramientas digitales"),
        (5, "Falta de capital humano capacitado"),
        (6, "Falta de estructura y organización interna"),
        (7, "Delincuencia"),
    )

    KNOWLEDGE_CHOICES = (
        (1, "1"),
        (2, "2"),
        (3, "3"),
        (4, "4"),
        (5, "5"),
        (6, "No Aplica"),
    )
    
    user_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name="Usuario")
    company_information = models.TextField(
        max_length=100, null=True, blank=True, 
        verbose_name="Datos de mi empresa/emprendimiento"
    )
    market = models.PositiveSmallIntegerField(
        choices=MARKET_CHOICES, null=True, blank=True, verbose_name="Mi Mercado es:"
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
    payment_vouchers = models.PositiveSmallIntegerField(
        choices=PAYMENT_CHOICES, null=True, blank=True, verbose_name="Emito comprobantes de pago"
    )
    main_challenges = models.PositiveSmallIntegerField(
        choices=PAYMENT_CHOICES, null=True, blank=True, verbose_name="Emito comprobantes de pago"
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


    def __str__(self):
        return self.company_information
    

class CompanyBrand(models.Model):
    BRAND_NAME_REGISTERED_CHOICES = (
        (1, "Sí"),
        (2, "No"),
        (3, "Prefiero no decirlo"),
    )

    user_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name="Usuario")
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
    goals_achieve = models.JSONField(
        blank=True, 
        null=True, 
        verbose_name="Mis metas a conseguir son"
    )
    digital_media = models.IntegerField(
        blank=True, 
        null=True, 
        verbose_name="¿Los medios digitales/físicos en los que tengo presencia me están ayudando a conseguir mis metas?"
    )

    def __str__(self):
        return self.brand_information

    
