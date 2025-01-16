from django.db import models

class Branch(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)  # Автоматическое добавление времени создания
    updated_at = models.DateTimeField(auto_now=True)      # Автоматическое обновление времени
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = "Branches"

    def mark_inactive(self):
        """Дополнительный метод для деактивации объекта."""
        self.is_active = False
        self.save()

    def mark_active(self):
        """Дополнительный метод для деактивации объекта."""
        self.is_active = True
        self.save()

    def __str__(self):
        return self.name