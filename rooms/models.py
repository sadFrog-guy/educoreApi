from django.db import models
from django.utils.translation import gettext_lazy as _

from utils.models import BaseModel


class Room(BaseModel):
    name = models.CharField(max_length=100, verbose_name=_("Name"))
    floor = models.IntegerField(verbose_name=_("Floor"))

    def __str__(self):
        return f'{self.name} {self.floor}'

    class Meta:
        verbose_name = _("Room")
        verbose_name_plural = _("Rooms")