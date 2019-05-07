
from django.db import models

from app.core.models import CreateUpdateModel, UUIDUser
from app.edu.models import Student

# Requirement
# - - - - - - - - - - - - - - - - - - -
class Requirement(CreateUpdateModel):
    STATUS = (
        (1, 'Deferido'),
        (2, 'Indeferido')
    ) 

    MEAL = (
        (1, 'Almoço'),
        (2, 'Jantar')
    )

    date = models.DateField()
    meal = models.IntegerField (choices = MEAL, verbose_name='Tipo de Refeição')
    status = models.IntegerField(choices = STATUS, verbose_name='Situação')
    justification_teacher = models.TextField(verbose_name='Justificativa do Requerente')
    justification_CAEST = models.TextField(verbose_name='Jusiticativa da CAEST')
    teacher = models.ForeignKey(UUIDUser, on_delete=models.CASCADE, related_name='requirements', verbose_name='Professor')
    evaluator = models.ForeignKey(UUIDUser, on_delete=models.CASCADE, related_name='evaluations', verbose_name='Avaliador da CAEST', null = True)

    def __str__(self):
        return f'{self.UUIDUser.first_name} ({self.UUIDUser.registration})'


    class Meta:
        verbose_name = 'solicitação'
        verbose_name_plural = 'solicitações'

#StudentMeal
# - - - - - - - - - - - - - - - - - - - 
class StudentMeal(CreateUpdateModel):
    MEAL = (
        (1, 'Almoço'),
        (2, 'Jantar')
    )

    date = models.DateField()
    meal = models.IntegerField (choices = MEAL, verbose_name='Tipo de Refeição')
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='student_meals', verbose_name='Aluno')
     
    def __str__(self):
        return f'{self.date} ({self.teacher.meal})'
    
    class Meta:
        verbose_name = 'refeição'
        verbose_name_plural = 'refeições'
