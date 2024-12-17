from django.db import models

from django.db import models

class Barbeiro(models.Model):
    idBarbeiro = models.AutoField(primary_key=True)
    NomeBarbeiro = models.CharField(max_length=255, null=False)
    telefoneBarbeiro = models.CharField(max_length=255, blank=True, null=True)
    fotoBarbeiro = models.ImageField(upload_to='barbeiro/', blank=True)

    def __str__(self):
        return self.NomeBarbeiro

class Barbearia(models.Model):
    nome = models.CharField(max_length=255, null=False)
    endereco = models.CharField(max_length=255, blank=True, null=True)
    idBarbearia = models.AutoField(primary_key=True)
    hrAbertura = models.CharField(max_length=255, blank=True, null=True)
    hrFechamento = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.nome

class Cliente(models.Model):
    idCliente = models.AutoField(primary_key=True)
    nomeCliente = models.CharField(max_length=255, null=False)
    telefoneCliente = models.CharField(max_length=255, blank=True, null=True)
    emailCliente = models.CharField(max_length=255, blank=True, null=True)
    sexoCliente = models.CharField(max_length=1, blank=True, null=True)
    barbeiroPreferido = models.CharField(max_length=255, blank=True, null=True)
    fotoCliente = models.ImageField(upload_to='cliente/')

    def __str__(self):
        return self.nomeCliente

class Trabalha(models.Model):
    idBarbeiro = models.ForeignKey(Barbeiro, on_delete=models.CASCADE, verbose_name="Barbeiro", default=1)
    idBarbearia = models.ForeignKey(Barbearia, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.idBarbeiro.NomeBarbeiro} trabalha na {self.idBarbearia.nome}"

class Agenda(models.Model):
    barbearia = models.ForeignKey('Barbearia', on_delete=models.CASCADE, verbose_name="Barbearia")
    nome = models.CharField(max_length=100, verbose_name="Nome da Agenda")
    barbeiro = models.ForeignKey('Barbeiro', on_delete=models.CASCADE, verbose_name="Barbeiro")
    data = models.DateField(verbose_name="Data")
    HORARIOS = (
        ("08:00-09:00", "08:00 às 09:00"),
        ("09:00-10:00", "09:00 às 10:00"),
        ("10:00-11:00", "10:00 às 11:00"),
        ("13:00-14:00", "13:00 às 14:00"),
        ("14:00-15:00", "14:00 às 15:00"),
        ("15:00-16:00", "15:00 às 16:00"),
        ("16:00-17:00", "16:00 às 17:00"),
        ("17:00-18:00", "17:00 às 18:00"),
        ("18:00-19:00", "18:00 às 19:00"),
    )
    horario = models.CharField(max_length=11, choices=HORARIOS, verbose_name="Horário")

    def __str__(self):
        return f'{self.barbeiro} - {self.data} - {self.get_horario_display()}'

class Agendamento(models.Model):
    agenda = models.ForeignKey(Agenda, on_delete=models.CASCADE, verbose_name="Agenda")
    cliente = models.ForeignKey('Cliente', on_delete=models.CASCADE, verbose_name="Cliente")

    def __str__(self):
        return f'{self.agenda} - {self.cliente}'
