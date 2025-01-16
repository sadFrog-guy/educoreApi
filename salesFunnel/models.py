from django.db import models

from utils.models import BaseModel


# Create your models here.
class SalesFunnelStage(BaseModel):
    """
    Модель для этапов воронки продаж.
    Например: "Пришел", "Согласился на пробный урок", "Прошел пробный урок", "Записался на курс" и т.д.
    """
    name = models.CharField(max_length=100, unique=True, verbose_name="Название этапа")
    order = models.PositiveIntegerField(verbose_name="Порядок этапа")

    class Meta:
        ordering = ['order']
        verbose_name = "Этап воронки"
        verbose_name_plural = "Этапы воронки"

    def __str__(self):
        return self.name

class Lead(BaseModel):
    """
    Модель для потенциального ученика.
    """
    first_name = models.CharField(max_length=50, verbose_name="Имя")
    last_name = models.CharField(max_length=50, verbose_name="Фамилия")
    email = models.EmailField(verbose_name="Email", null=True, blank=True)
    phone = models.CharField(max_length=20, blank=True, verbose_name="Телефон", null=True)
    current_stage = models.ForeignKey(
        SalesFunnelStage,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Текущий этап"
    )

    class Meta:
        verbose_name = "Лид"
        verbose_name_plural = "Лиды"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class FunnelAction(BaseModel):
    """
    Модель для записи действий лида в воронке.
    Например, переходы между этапами, прохождение теста и т.д.
    """
    lead = models.ForeignKey(Lead, on_delete=models.CASCADE, verbose_name="Лид")
    stage = models.ForeignKey(SalesFunnelStage, on_delete=models.CASCADE, verbose_name="Этап")
    note = models.TextField(blank=True, verbose_name="Комментарий")

    class Meta:
        verbose_name = "Действие воронки"
        verbose_name_plural = "Действия воронки"

    def __str__(self):
        return f"{self.lead} - {self.stage.name} ({self.created_at})"
