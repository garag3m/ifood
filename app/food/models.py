from django.db import models

from app.core.models import CreateUpdateModel, UUIDUser


# Requirement
# - - - - - - - - - - - - - - - - - - -
class Requirement(CreateUpdateModel):

    date = models.DateField()
    meal = models.CharField(max_length=20, verbose_name='Refeição')
    status = models.CharField(max_length=100, verbose_name='Matrícula')
    justification_teacher = models.TextField(verbose_name='Justificativa do Requerente')
    justification_CAEST = models.TextField(verbose_name='Jusiticativa da CAEST')
    teacher = models.ForeignKey(UUIDUser, on_delete=models.CASCADE, related_name='requirements', verbose_name='Professor')

    def __str__(self):
        return f'{self.teacher.first_name} ({self.teacher.registration})'

    class Meta:
        verbose_name = 'solicitação'
        verbose_name_plural = 'solicitações'

#Student_Meal
# - - - - - - - - - - - - - - - - - - - 
class Student_Meal(CreateUpdateModel):

    date = models.DateField()
    meal = models.CharField(max_length=20, verbose_name='Refeição')
    student = models.ForeignKey(UUIDUser, on_delete=models.CASCADE, related_name='student_meals', verbose_name='Aluno')
     
    def __str__(self):
        return f'{self.date} ({self.teacher.meal})'
    
    class Meta:
        verbose_name = 'refeição'
        verbose_name_plural = 'refeições'
