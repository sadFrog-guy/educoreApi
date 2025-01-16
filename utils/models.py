from django.db import models

class BaseModel(models.Model):
    branch = models.ForeignKey('branches.Branch', on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True

    def mark_inactive(self):
        self.is_active = False
        self.save()

    def mark_active(self):
        self.is_active = True
        self.save()