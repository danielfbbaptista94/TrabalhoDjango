from django.db import models
from multiselectfield import MultiSelectField
from datetime import date


class Clientes(models.Model):
    razaSocial = models.CharField(max_length=50)
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

    class Meta:
        verbose_name_plural = "Clientes"


class Empresas(models.Model):
    razaSocial = models.CharField(max_length=50)
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

    class Meta:
        verbose_name_plural = 'Empresas'


class Fornecedores(models.Model):
    razaSocial = models.CharField(max_length=50)
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

    class Meta:
       verbose_name_plural = 'Fornecedores'


class FormaPagamentos(models.Model):
    descricao = models.CharField(max_length=50)

    def __str__(self):
        return self.descricao

    class Meta:
        verbose_name_plural = 'Formas de Pagamentos'


class ContasBancarias(models.Model):
    contasList = (('Caixa', 'Caixa'), ('Banco', 'Banco'))

    classificacao = models.CharField(max_length=18)
    descricao = models.CharField(max_length=50)
    numeroConta = models.CharField(max_length=20)
    numeroAgencia = models.CharField(max_length=20)
    dataSaldoInicial = models.DateField(default=date.today)
    saldoInicial = models.CharField(max_length=14)
    tipo = MultiSelectField(choices=contasList, max_choices=1)

    def __str__(self):
        return self.descricao

    class Meta:
        verbose_name_plural = "Contas Bancarias"


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

    class Meta:
        verbose_name_plural = "Plano de Contas"


class LancamentosReceber(models.Model):
    cliente = models.ForeignKey(Clientes, on_delete=models.CASCADE)
    empresa = models.ForeignKey(Empresas, on_delete=models.CASCADE)
    dataVencimento = models.DateField(default=date.today)
    dataEmissao = models.DateField(default=date.today)
    numeroDocumento = models.CharField(max_length=5)
    valorTitulo = models.FloatField(max_length=5)

    def __str__(self):
        return self.empresa


class LancamentosReceber(models.Model):
    Clientes = models.ForeignKey(Clientes, on_delete=models.CASCADE)
    Empresas = models.ForeignKey(Empresas, on_delete=models.CASCADE)
    dataVencimento = models.DateField(default=date.today)
    datEmissao = models.DateField(default=date.today)
    valorTitulo = models.FloatField(max_length=5)
    numeroDocumento = models.IntegerField()

    def __str__(self):
        return self.descricao

    class Meta:
        verbose_name_plural = "Lancamentos a Receber"


class BaixasReceber(models.Model):
    empresa = models.ForeignKey(LancamentosReceber, on_delete=models.CASCADE)
    caixaBanco = models.ForeignKey(FormaPagamentos, on_delete=models.CASCADE)
#   banco
    vencimentoPagamento = models.DateField(default=date.today)
    disponibilidade = models.DateField(default=date.today)
    dataBaixa = models.DateField(default=date.today)
    numeroDocumento = models.CharField(max_length=5)
    valorRecebido = models.FloatField(max_length=5)
    valorResidual = models.FloatField(max_length=5)

    class Meta:
        verbose_name_plural = "Baixa de Conta a Receber"


class LancamentosPagar(models.Model):
    fk_Fornecedores = models.ForeignKey(Fornecedores, on_delete=models.CASCADE)
    fk_Empresas = models.ForeignKey(Empresas, on_delete=models.CASCADE)
    dataVencimento = models.DateField(default=date.today)
    datEmissao = models.DateField(default=date.today)
    valorTitulo = models.FloatField(max_length=5)
    numeroDocumento = models.IntegerField()

    def __str__(self):
        return self.descricao

    class Meta:
        verbose_name_plural = "Lancamentos a Pagar"


class BaixasPagar(models.Model):
    empresa = models.ForeignKey(LancamentosPagar, on_delete=models.CASCADE)
    caixaBanco = models.ForeignKey(FormaPagamentos, on_delete=models.CASCADE)
#   banco
    vencimentoPagamento = models.DateField(default=date.today)
    disponibilidade = models.DateField(default=date.today)
    dataBaixa = models.DateField(default=date.today)
    numeroDocumento = models.CharField(max_length=5)
    valorRecebido = models.FloatField(max_length=5)
    valorResidual = models.FloatField(max_length=5)

    class Meta:
        verbose_name_plural = "Baixa de Conta a Pagar"


class Tesouraria(models.Model):
    fk_Empresas = models.ForeignKey(Empresas, on_delete=models.CASCADE)
    fk_Clientes = models.ForeignKey(Clientes, on_delete=models.CASCADE)
    fk_PlanoContas = models.ForeignKey(PlanoContas, on_delete=models.CASCADE)
    fk_FormaPagamentos = models.ForeignKey(FormaPagamentos, on_delete=models.CASCADE)
    fk_Fornecedores = models.ForeignKey(Fornecedores, on_delete=models.CASCADE)
    valor = models.FloatField(max_length=5)
    numero = models.IntegerField()
    datEmissao = models.DateField(default=date.today)
    dataVencimento = models.DateField(default=date.today)
    dataDisponibilidade = models.DateField(default=date.today)

    class Meta:
        verbose_name_plural = "Tesouraria"
