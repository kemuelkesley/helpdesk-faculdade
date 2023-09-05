from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Ticket(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50, verbose_name="Título")
    description = models.TextField(verbose_name="Descrição")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Data de Abertura")
    closed_at = models.DateTimeField(null=True, blank=True, verbose_name="Data de Fechamento")
    user = models.ForeignKey("auth.User", on_delete=models.CASCADE, verbose_name="Usuário")
    
    status = models.CharField(max_length=10, choices=(
        ("aberto", "Aberto"),
        ("fechado", "Fechado"),
    ), default="aberto", verbose_name="Status")

    def __str__(self):
        return self.title
    
     # Campo para armazenar o número do ticket
    #numero_ticket = models.CharField(max_length=10, unique=True, editable=False)
    # def save(self, *args, **kwargs):
    #         # Verifica se o ticket está sendo criado (não tem um número de ticket)
    #         if not self.numero_ticket:
    #             # Calcula o próximo número de ticket com base no total de tickets existentes
    #             ultimo_ticket = Ticket.objects.last()
    #             if ultimo_ticket:
    #                 ultimo_numero_ticket = int(ultimo_ticket.numero_ticket)
    #                 novo_numero_ticket = str(ultimo_numero_ticket + 1)
    #             else:
    #                 novo_numero_ticket = "1"
    #             self.numero_ticket = novo_numero_ticket

    #         super().save(*args, **kwargs)


    class Meta:
        verbose_name = "Chamado"
        verbose_name_plural = "Abertura de Chamados"
        ordering = ["-created_at"]



class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey("auth.User", on_delete=models.CASCADE)

    def __str__(self):
        return self.comment

    class Meta:
        verbose_name = "Comentário"
        verbose_name_plural = "Comentários"
        ordering = ["-created_at"]


class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"
        ordering = ["name"]


