from django.db import models

# Create your models here.

class Ticket(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    closed_at = models.DateTimeField(null=True, blank=True)
    user = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    
    status = models.CharField(max_length=10, choices=(
        ("aberto", "Aberto"),
        ("fechado", "Fechado"),
    ), default="open")

    def __str__(self):
        return self.title
    
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

