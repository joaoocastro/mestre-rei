from django.db import models

class Barbeiro(models.Model):
    idBarbeiro = models.AutoField(primary_key=True)
    NomeBarbeiro = models.CharField(max_length=255, null=False)
    telefoneBarbeiro = models.CharField(max_length=255, blank=True, null=True)
    fotoBarbeiro = models.CharField(max_length=255, blank=True, null=True)

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
    fotoCliente = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.nomeCliente

class Trabalha(models.Model):
    idBarbeiro = models.ForeignKey(Barbeiro, on_delete=models.CASCADE, primary_key=True)
    idBarbearia = models.ForeignKey(Barbearia, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.idBarbeiro.NomeBarbeiro} trabalha na {self.idBarbearia.nome}"

class Agendamento(models.Model):
    dataCompleta = models.DateField(null=False)
    idAgendamento = models.AutoField(primary_key=True)
    idBarbeiro = models.ForeignKey(Barbeiro, on_delete=models.CASCADE)
    idCliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    idBarbearia = models.ForeignKey(Barbearia, on_delete=models.CASCADE)

    def __str__(self):
        return f"Agendamento {self.idAgendamento} - {self.dataCompleta}"

