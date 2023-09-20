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

    descricao = models.CharField(
        max_length=50,
        null=True,
        blank=True,
        verbose_name="Descrição",
    )

    condominio = models.ForeignKey(
        Condominio,
        on_delete=models.CASCADE,
        verbose_name="Condomínio",
        related_name="equipamentos",
        null=True
    )
    
    data_compra = models.DateField(
        null=True, 
        blank=True,
        verbose_name='Data de Compra',
        help_text='Exemplo de data: 01/01/2023',
    )
   
    data_fim_garantia = models.DateField(
        null=True, 
        blank=True,
        verbose_name='Data Fim de Garantia',        
    )
    
    dia_recebimento = models.DateField(
        null=True, 
        blank=True,
        verbose_name='Dia de Recebimento',       
    )

    data_instalacao = models.DateField(
        null=True, 
        blank=True,
        verbose_name='Data de Instalação',       
    )
   
   
    testado = models.BooleanField(
        default=False,
        verbose_name="Testado",
    )

    def __str__(self):
       return self.nome
