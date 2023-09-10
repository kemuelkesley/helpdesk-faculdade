from django.db import models

# Create your models here.

class Condominio(models.Model):
       

    numero_identificacao = models.PositiveIntegerField(
        verbose_name="Número de Identificação",
        help_text="Número de identificação do condomínio",
        unique=True,   # Garante que não haja repetição de valores
        blank=False    # Garante que o campo não pode ser vazio
    )
    
    nome = models.CharField(
        max_length=50, 
        blank=False,
        verbose_name="Nome do Condominio",
        help_text="Infome o nome do Condominio",
        #unique=True,   # Garante que não haja repetição de valores
    )

    #criado_em = models.DateTimeField(auto_now_add=True, editable=False, blank=True)

    def __str__(self):
       return f'{self.numero_identificacao} - {self.nome}' 
       
