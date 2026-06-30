from django.db import models

class atendimentos(models.Model):

    STATUS = [
        ("P", "Pendente"),
        ("A", "Andamento"),
        ("C", "Concluída"),
    ]

    nome = models.CharField(max_length=100)
    status = models.CharField(max_length=1, choices=STATUS)
    prazo = models.DateField()

    def __str__(self):
        return self.nome