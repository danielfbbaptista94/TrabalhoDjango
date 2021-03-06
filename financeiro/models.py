from django.db import models
from multiselectfield import MultiSelectField
from datetime import datetime
from django.urls import reverse


class Clientes(models.Model):
    razaoSocial = models.CharField(max_length=50)
    identificacao = models.CharField(max_length=50)
    classificacao = models.CharField(max_length=50)
    tipoPessoa = models.CharField(max_length=10)
    cnpjCpf = models.CharField(max_length=15)
    inscricaoEstadual = models.CharField(max_length=20)
    inscricaoMunicipal = models.CharField(max_length=20)
    endereco = models.CharField(max_length=50)
    bairro = models.CharField(max_length=50)
    municipio = models.CharField(max_length=50)
    cep = models.CharField(max_length=10)
    uf = models.CharField(max_length=2)
    telefone = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    nome_titular = models.CharField(max_length=50)
    cpf = models.CharField(max_length=15)
    funcao = models.CharField(max_length=50)

    def __str__(self):
        return self.razaoSocial

    class Meta:
        verbose_name_plural = "Clientes"

    def get_absolute_url(self):
        return reverse('financeiro-home', kwargs={'pk': self.pk})


class Empresas(models.Model):
    razaoSocial = models.CharField(max_length=50)
    identificacao = models.CharField(max_length=50)
    tipoPessoa = models.CharField(max_length=10)
    cnpj = models.CharField(max_length=15)
    inscricaoEstadual = models.CharField(max_length=20)
    inscricaoMunicipal = models.CharField(max_length=20)
    endereco = models.CharField(max_length=50)
    bairro = models.CharField(max_length=50)
    municipio = models.CharField(max_length=50)
    cep = models.CharField(max_length=10)
    uf = models.CharField(max_length=2)
    telefone = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    nome_titular = models.CharField(max_length=50)
    cpf = models.CharField(max_length=15)
    funcao = models.CharField(max_length=50)

    def __str__(self):
        return self.razaoSocial

    class Meta:
        verbose_name_plural = 'Empresas'

    def get_absolute_url(self):
        return reverse('financeiro-home', kwargs={'pk': self.pk})


class Fornecedores(models.Model):
    razaoSocial = models.CharField(max_length=50)
    identificacao = models.CharField(max_length=50)
    classificacao = models.CharField(max_length=50)
    tipoPessoa = models.CharField(max_length=10)
    cnpjCpf = models.CharField(max_length=15)
    inscricaoEstadual = models.CharField(max_length=20)
    inscricaoMunicipal = models.CharField(max_length=20)
    endereco = models.CharField(max_length=50)
    bairro = models.CharField(max_length=50)
    municipio = models.CharField(max_length=50)
    cep = models.CharField(max_length=10)
    uf = models.CharField(max_length=2)
    telefone = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    nome_titular = models.CharField(max_length=50)
    cpf = models.CharField(max_length=15)
    funcao = models.CharField(max_length=50)

    def __str__(self):
        return self.razaoSocial

    class Meta:
       verbose_name_plural = 'Fornecedores'

    def get_absolute_url(self):
        return reverse('financeiro-home', kwargs={'pk': self.pk})


class FormaPagamentos(models.Model):
    descricao = models.CharField(max_length=50)

    def __str__(self):
        return self.descricao

    class Meta:
        verbose_name_plural = 'Formas de Pagamentos'

    def get_absolute_url(self):
        return reverse('financeiro-home', kwargs={'pk': self.pk})


class ContasBancarias(models.Model):
    contasList = (('Caixa', 'Caixa'), ('Banco', 'Banco'))

    classificacao = models.CharField(max_length=18)
    descricao = models.CharField(max_length=50)
    numeroConta = models.CharField(max_length=20)
    numeroAgencia = models.CharField(max_length=20)
    dataSaldoInicial = models.DateField(default=datetime.now())
    saldoInicial = models.CharField(max_length=14)
    tipo = MultiSelectField(choices=contasList, max_choices=1)

    def __str__(self):
        return self.descricao

    class Meta:
        verbose_name_plural = "Contas Bancarias"

    def get_absolute_url(self):
        return reverse('financeiro-home', kwargs={'pk': self.pk})


class PlanoContas(models.Model):
    caractList = (('Caixa', 'Caixa'),
                  ('Banco', 'Banco'),
                  ('Cliente', 'Cliente'),
                  ('Fornecedor', 'Fornecedor'),
                  ('Entrade de Recursos', 'Entrade de Recursos'),
                  ('Saída de Recursos', 'Saída de Recursos')
    )

    conta = models.ForeignKey(ContasBancarias, on_delete=models.CASCADE)
    classificacao = models.CharField(max_length=20)
    descricao = models.CharField(max_length=14)
    tipo = models.CharField(max_length=15)
    caracteristica = MultiSelectField(choices=caractList)

    def __str__(self):
        return self.descricao

    class Meta:
        verbose_name_plural = "Plano de Contas"

    def get_absolute_url(self):
        return reverse('financeiro-home', kwargs={'pk': self.pk})


class LancamentosReceber(models.Model):
    cliente = models.ForeignKey(Clientes, on_delete=models.CASCADE)
    empresa = models.ForeignKey(Empresas, on_delete=models.CASCADE)
    dataVencimento = models.DateField(default=datetime.now())
    dataEmissao = models.DateField(default=datetime.now())
    numeroDocumento = models.CharField(max_length=5)
    valorTitulo = models.FloatField(max_length=5)

    def __str__(self):
        return self.empresa

    class Meta:
        verbose_name_plural = "Lancamentos a Receber"

    def get_absolute_url(self):
        return reverse('financeiro-home', kwargs={'pk': self.pk})


class BaixasReceber(models.Model):
    empresa = models.ForeignKey(LancamentosReceber, on_delete=models.CASCADE)
    FormaPagamento = models.ForeignKey(FormaPagamentos, on_delete=models.CASCADE)
    CaixaBanco = models.ForeignKey(PlanoContas, on_delete=models.CASCADE, null=True)
    vencimentoPagamento = models.DateField(default=datetime.now())
    disponibilidade = models.DateField(default=datetime.now())
    dataBaixa = models.DateField(default=datetime.now())
    numeroDocumento = models.CharField(max_length=5)
    valorRecebido = models.FloatField(max_length=5)
    valorResidual = models.FloatField(max_length=5)

    def __str__(self):
        return self.empresa

    class Meta:
        verbose_name_plural = "Baixa de Conta a Receber"

    def get_absolute_url(self):
        return reverse('financeiro-home', kwargs={'pk': self.pk})


class LancamentosPagar(models.Model):
    Fornecedores = models.ForeignKey(Fornecedores, on_delete=models.CASCADE)
    empresa = models.ForeignKey(Empresas, on_delete=models.CASCADE)
    dataVencimento = models.DateField(default=datetime.now())
    dataEmissao = models.DateField(default=datetime.now())
    numeroDocumento = models.CharField(max_length=5)
    valorTitulo = models.FloatField(max_length=5)

    def __str__(self):
        return self.Empresas

    class Meta:
        verbose_name_plural = "Lancamentos a Pagar"

    def get_absolute_url(self):
        return reverse('financeiro-home', kwargs={'pk': self.pk})


class BaixasPagar(models.Model):
    Empresa = models.ForeignKey(LancamentosPagar, on_delete=models.CASCADE)
    FormaPagamento = models.ForeignKey(FormaPagamentos, on_delete=models.CASCADE)
    CaixaBanco = models.ForeignKey(PlanoContas, on_delete=models.CASCADE, null=True)
    VencimentoPagamento = models.DateField(default=datetime.now())
    Disponibilidade = models.DateField(default=datetime.now())
    DataBaixa = models.DateField(default=datetime.now())
    NumeroDocumento = models.CharField(max_length=5)
    ValorRecebido = models.FloatField(max_length=5)
    ValorResidual = models.FloatField(max_length=5)

    def __str__(self):
        return self.Empresa

    class Meta:
        verbose_name_plural = "Baixa de Conta a Pagar"

    def get_absolute_url(self):
        return reverse('financeiro-home', kwargs={'pk': self.pk})


class Tesouraria(models.Model):
    Empresas = models.ForeignKey(Empresas, on_delete=models.CASCADE)
    Clientes = models.ForeignKey(Clientes, on_delete=models.CASCADE)
    Fornecedores = models.ForeignKey(Fornecedores, on_delete=models.CASCADE)
    Entrada = models.ForeignKey(PlanoContas, related_name='conta_entrada', on_delete=models.CASCADE, null=True)
    Saida = models.ForeignKey(PlanoContas, related_name='conta_saida', on_delete=models.CASCADE, null=True)
    FormaPagamentos = models.ForeignKey(FormaPagamentos, on_delete=models.CASCADE)
    valor = models.FloatField(max_length=5)
    numero = models.IntegerField()
    dataEmissao = models.DateField(default=datetime.now())
    dataVencimento = models.DateField(default=datetime.now())
    dataDisponibilidade = models.DateField(default=datetime.now())

    def __str__(self):
        return self.Empresas

    class Meta:
        verbose_name_plural = "Tesouraria"

    def get_absolute_url(self):
        return reverse('financeiro-home', kwargs={'pk': self.pk})
