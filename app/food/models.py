from django.db import models

from app.core.models import CreateUpdateModel, UUIDUser


# Requirement
# - - - - - - - - - - - - - - - - - - -
class Requirement(CreateUpdateModel):

    date = models.DateField()
    justification = models.TextField(verbose_name='jusiticativa')
    teacher = models.ForeignKey(UUIDUser, on_delete=models.CASCADE, related_name='requirements', verbose_name='Professor')

    def __str__(self):
        return f'{self.teacher.first_name} ({self.teacher.registration})'

    class Meta:
        verbose_name = 'solicitação'
        verbose_name_plural = 'solicitações'