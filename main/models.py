from django.db import models

class Aluno(models.Model):
    nome = models.CharField(max_length=255)
    email = models.EmailField()
    telefone = models.CharField(max_length=15)
    data_nascimento = models.DateField(null=True)
    description = models.TextField()
    
    def __str__(self):
        return self.nome

