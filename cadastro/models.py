from django.db import models

# Create your models here.

class Condominio(models.Model):
       

    numero_identificacao = models.PositiveIntegerField(
        verbose_name="Conta",
        help_text="Número de identificação",
        unique=True,   # Garante que não haja repetição de valores
        blank=False    # Garante que o campo não pode ser vazio
    )
    
    nome = models.CharField(
        max_length=50, 
        blank=False,
        verbose_name="Nome do Condominio",
        help_text="Infome o nome",
        #unique=True,   # Garante que não haja repetição de valores
    )

    endereco = models.CharField(
        max_length=50, 
        blank=True,
        null=True,
        verbose_name="Endereço",
        help_text="Infome o endereço",
    )
    

    #criado_em = models.DateTimeField(auto_now_add=True, editable=False, blank=True)
    

    def __str__(self):
       return f'{self.numero_identificacao} - {self.nome}' 
       #return self.nome


class CategoriaEquipamento(models.Model):

    codigo = models.CharField(
        max_length=10, 
        unique=True,
        blank=False, 
        verbose_name="Código da Categoria"
    )


    nome = models.CharField(
        max_length=50, 
        blank=False, 
        verbose_name="Nome da Categoria"
    )


    criado_em = models.DateTimeField(
        auto_now_add=True, 
        editable=False, 
        verbose_name="Criação Em"
    )

  

    def __str__(self):
        return self.nome
    

    class Meta:
        verbose_name = "Categoria de equipamentos"
        verbose_name_plural = "Categoria"
        ordering = ["-criado_em"]



class Equipamento(models.Model):
    nome = models.CharField(
        max_length=50,
        blank=False,
        verbose_name="Nome",
    )

    numero_serie = models.CharField(
        max_length=50,
        blank=False,
        verbose_name="Número de Série",
    )

    condominio = models.ForeignKey(
        Condominio,
        on_delete=models.CASCADE,
        verbose_name="Condomínio",
        related_name="equipamentos",
        null=True
    )


    categoria = models.ForeignKey(
        CategoriaEquipamento, 
        on_delete=models.CASCADE, 
        related_name="equipamentos", 
        verbose_name="Categoria",
        null=True
    )
    
    data_instalacao = models.DateField(
        null=True, 
        blank=True,
        verbose_name='Data de Instalação',
        help_text='Exemplo de data: 01/01/2023',
    )

   
    testado = models.BooleanField(
        default=False,
        verbose_name="Testado",
    )

    def __str__(self):
       return self.nome
