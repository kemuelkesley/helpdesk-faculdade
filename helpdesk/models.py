import locale
from django.db import models
from django.contrib.auth.models import User
from cadastro.models import Condominio
from django.utils import timezone


#from simple_history.models import HistoricalRecords

#Configura o locale para português do Brasil
locale.setlocale(locale.LC_TIME, 'pt_BR.utf8')

class Ticket(models.Model):
   
    title = models.CharField(max_length=50, verbose_name="Título")

    category = models.ForeignKey(
        "Category", 
        on_delete=models.CASCADE, 
        verbose_name="Categoria",
        null=True
    )

    description = models.TextField(verbose_name="Descrição")
    
    condominio = models.ForeignKey(
        Condominio, 
        on_delete=models.CASCADE, 
        verbose_name="Condomínio",
    )
   
  
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Data de Abertura")

    user = models.ForeignKey(
        "auth.User", 
        on_delete=models.CASCADE, 
        blank=True, null=True ,
        verbose_name = "Técnico"
    )
        
    # status = models.CharField(max_length=10, choices=(
    #     ("aberto", "Aberto"),
    #     ("andamento", "Andamento"),
    #     ("fechado", "Fechado"),
    # ), default="aberto", verbose_name="Status")

    STATUS_CHOICES = (
        ('aberto', 'Aberto'),
        ('andamento', 'Andamento'),
        ('fechado', 'Fechado'),
    )

    status = models.CharField(
        max_length=10, 
        choices=STATUS_CHOICES,
        default='aberto',
        verbose_name="Status"
    )

    closed_at = models.DateTimeField(null=True, blank=True, verbose_name="Data de Fechamento",)
  

    numero_chamado = models.PositiveIntegerField(
        unique=True, 
        verbose_name="Ticket",
        editable=False,
        blank=True,
        #default=1
    )


    def save(self, *args, **kwargs):
        if self.status == "fechado" and not self.closed_at:
            self.closed_at = timezone.now()
        
        if not self.numero_chamado:
            # Obtém o número do último chamado, se existir
            ultimo_chamado = Ticket.objects.order_by('-numero_chamado').first()
            if ultimo_chamado:
                self.numero_chamado = ultimo_chamado.numero_chamado + 1
            else:
                self.numero_chamado = 1

        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
    
    def get_condominio_nome(self):
        return self.condominio.nome

    def get_condominio_numero_identificacao(self):
        return self.condominio.numero_identificacao
        

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
    name = models.CharField(
        max_length=50, 
        verbose_name="Nome",
        blank=False,
        null=True,
        help_text="Criar categoria para o chamado"
    )

    descricao = models.CharField(
        max_length=50, 
        verbose_name="Descrição",
        blank=False,
        null=True,
        help_text="Criar descrição para a categoria"
    )

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"
        ordering = ["name"]


