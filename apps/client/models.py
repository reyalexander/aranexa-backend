from django.db import models
from apps.user.models import Account
from django.contrib.postgres.fields import ArrayField

class Client(models.Model):
    TYPE_CLIENT_CHOICES = (
        (1, "B2B (Vendo a otras empresas)"),
        (2, "B2C (Vendo a otras personas)"),
        (3, "B2B2C (Mi cliente final es a través de otro negocio)"),
        (4, "B2G (Le vendo al gobierno)"),
    )

    TARGET_AUDIENCE_CHOICES = (
        (1, "Sí"),
        (2, "No"),
        (3, "No estoy seguro(a)"),
    )

    account_id = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True, verbose_name="Usuario")
    client_type = models.PositiveSmallIntegerField(
        choices=TYPE_CLIENT_CHOICES,
        null=True,
        blank=True,
        verbose_name="Mi tipo de cliente es"
    )
    target_audience = models.PositiveSmallIntegerField(
        choices=TARGET_AUDIENCE_CHOICES,
        null=True,
        blank=True,
        verbose_name="¿Conozco quién es mi público objetivo más importante?"
    )
    recommendations = ArrayField(
        models.TextField(),
        size=10,
        null=True,
        blank=True, 
        verbose_name="Busco recomendaciones o sugerencias mediante"
    )

    def __str__(self):
        if self.client_type is None:
            return f"Client Type #{self.client_type}"
        return f"Client {self.id}"