from django.db import models
from apps.user.models import Account
from django.contrib.postgres.fields import ArrayField

class Product(models.Model):
    TYPE_PRODUCT_CHOICES = (
        (1, "Producto"),
        (2, "Servicio"),
        (3, "Producto y servicio")
    )

    CREATED_PRODUCT_FROM_CHOICES = (
        (1, "Alta demanda"),
        (2, "Ofrecer nuevas alternativas"),
        (3, "Rubro con poca competencia"),
        (4, "Legado familiar"),
        (5, "Aún no lo sé")
    )

    PRICE_APPROPIATE_CHOICES = (
        (1, "Sí, es el precio correcto"),
        (2, "No, tengo que actualizarlo"),
        (3, "No lo sé, no tengo referentes")
    )

    account_id = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True, verbose_name="Usuario")
    product_name = models.PositiveSmallIntegerField(
        choices=TYPE_PRODUCT_CHOICES,
        null=True,
        blank=True,
        verbose_name="Datos de mi producto/servicio"
    )
    product_description = models.TextField(
        null=True, 
        blank=True, 
        verbose_name="El producto/servicio que ofrezco es el siguiente"
    )
    created_product_from = models.PositiveSmallIntegerField(
        choices=CREATED_PRODUCT_FROM_CHOICES,
        null=True,
        blank=True,
        verbose_name="Mi producto/servicio lo creé a partir de"
    )
    product_invest = ArrayField(
        models.TextField(),
        size=10,
        null=True,
        blank=True,
        verbose_name="Para producir mi producto, invierto más en"
    )
    keep_product_track = ArrayField(
        models.TextField(),
        size=10,
        null=True,
        blank=True,
        verbose_name="Llevo un registro de cuentas de mi producto/servicio"
    )
    price_appropiate = models.PositiveSmallIntegerField(
        choices=PRICE_APPROPIATE_CHOICES,
        null=True,
        blank=True,
        verbose_name="Mi producto/servicio lo creé a partir de"
    )

    def __str__(self):
        return f"{self.product_name} -> {self.product_description}"
