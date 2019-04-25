from django.db import models

from app.core.models import CreateUpdateModel


# Student
# - - - - - - - - - - - - - - - - - - -
class Student(CreateUpdateModel):

    name = models.CharField(max_length=100, verbose_name='Nome')
    registration = models.CharField(max_length=100, verbose_name='Matrícula')
    remote_uuid = models.CharField(max_length=50, verbose_name='UUID SUAP')
    course = models.CharField(max_length=100, verbose_name='Curso')
    status = models.CharField(max_length=100, verbose_name='Situação')

    def __str__(self):
        return f'{self.name} ({self.registration})'

    class Meta:
        verbose_name = 'aluno'
        verbose_name_plural = 'alunos'

# User
# - - - - - - - - - - - - - - - - - - -
class User(CreateUpdateModel):

    registration = models.CharField(max_length=100, verbose_name='Matrícula')
    password = models.CharField(max_length=20, verbose_name='Senha')
    name = models.CharField(max_length=100, verbose_name='Nome')
    email = models.CharField(max_length=100, verbose_name='E-mail')
    function = models.CharField(max_length=100, verbose_name='Tipo de Usuário')

    def __str__(self):
        return f'{self.name} ({self.registration})'

    class Meta:
        verbose_name = 'usuário'
        verbose_name_plural = 'usuários'
