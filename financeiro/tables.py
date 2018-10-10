import django_tables2 as tables
from django_tables2 import A
from .models import LancamentosReceber, LancamentosPagar, BaixasReceber, BaixasPagar, Tesouraria


class LancamentosReceberTable(tables.Table):
    cliente = tables.LinkColumn('lancamentosreceber-details', args=[A('pk')])
    empresa = tables.LinkColumn('lancamentosreceber-details', args=[A('pk')])
    dataVencimento = tables.LinkColumn('lancamentosreceber-details', args=[A('pk')])
    dataEmissao = tables.LinkColumn('lancamentosreceber-details', args=[A('pk')])
    numeroDocumento = tables.LinkColumn('lancamentosreceber-details', args=[A('pk')])
    valorTitulo = tables.LinkColumn('lancamentosreceber-details', args=[A('pk')])

    class Meta:
        model = LancamentosReceber
        fields = ('cliente', 'empresa', 'dataVencimento', 'dataEmissao', 'numeroDocumento', 'valorTitulo')
        attrs = {"class": "table-striped table-bordered"}
        empty_text = "Não tem dados..."


class LancamentosPagarTable(tables.Table):
    Fornecedores = tables.LinkColumn('lancamentospagar-details', args=[A('pk')])
    empresa = tables.LinkColumn('lancamentospagar-details', args=[A('pk')])
    dataVencimento = tables.LinkColumn('lancamentospagar-details', args=[A('pk')])
    dataEmissao = tables.LinkColumn('lancamentospagar-details', args=[A('pk')])
    numeroDocumento = tables.LinkColumn('lancamentospagar-details', args=[A('pk')])
    valorTitulo = tables.LinkColumn('lancamentospagar-details', args=[A('pk')])

    class Meta:
        model = LancamentosPagar
        fields = ('Fornecedores', 'empresa', 'dataVencimento', 'dataEmissao', 'numeroDocumento', 'valorTitulo')
        attrs = {"class": "table-striped table-bordered"}
        empty_text = "Não tem dados..."


class BaixasReceberTable(tables.Table):
    empresa = tables.LinkColumn('baixasreceber-details', args=[A('pk')])
    FormaPagamento = tables.LinkColumn('baixasreceber-details', args=[A('pk')])
    CaixaBanco = tables.LinkColumn('baixasreceber-details', args=[A('pk')])
    vencimentoPagamento = tables.LinkColumn('baixasreceber-details', args=[A('pk')])
    disponibilidade = tables.LinkColumn('baixasreceber-details', args=[A('pk')])
    dataBaixa = tables.LinkColumn('baixasreceber-details', args=[A('pk')])
    numeroDocumento = tables.LinkColumn('baixasreceber-details', args=[A('pk')])
    valorRecebido = tables.LinkColumn('baixasreceber-details', args=[A('pk')])
    valorResidual = tables.LinkColumn('baixasreceber-details', args=[A('pk')])

    class Meta:
        model = BaixasReceber
        fields = ('empresa', 'FormaPagamento', 'CaixaBanco', 'vencimentoPagamento', 'disponibilidade',
                    'dataBaixa', 'numeroDocumento', 'valorRecebido', 'valorResidual')
        attrs = {"class": "table-striped table-bordered"}
        empty_text = "Não tem dados..."


class BaixasPagarTable(tables.Table):
    Empresa = tables.LinkColumn('baixaspagar-details', args=[A('pk')])
    FormaPagamento = tables.LinkColumn('baixaspagar-details', args=[A('pk')])
    CaixaBanco = tables.LinkColumn('baixaspagar-details', args=[A('pk')])
    VencimentoPagamento = tables.LinkColumn('baixaspagar-details', args=[A('pk')])
    Disponibilidade = tables.LinkColumn('baixaspagar-details', args=[A('pk')])
    DataBaixa = tables.LinkColumn('baixaspagar-details', args=[A('pk')])
    NumeroDocumento = tables.LinkColumn('baixaspagar-details', args=[A('pk')])
    ValorRecebido = tables.LinkColumn('baixaspagar-details', args=[A('pk')])
    ValorResidual = tables.LinkColumn('baixaspagar-details', args=[A('pk')])

    class Meta:
        model = BaixasPagar
        fields = ('Empresa', 'FormaPagamento', 'CaixaBanco', 'VencimentoPagamento', 'Disponibilidade',
                    'DataBaixa', 'NumeroDocumento', 'ValorRecebido', 'ValorResidual')
        attrs = {"class": "table-striped table-bordered"}
        empty_text = "Não tem dados..."


class TesourariaTable(tables.Table):
    Empresas = tables.LinkColumn('tesouraria-details', args=[A('pk')])
    Clientes = tables.LinkColumn('tesouraria-details', args=[A('pk')])
    Fornecedores = tables.LinkColumn('tesouraria-details', args=[A('pk')])
    Entrada = tables.LinkColumn('tesouraria-details', args=[A('pk')])
    Saida = tables.LinkColumn('tesouraria-details', args=[A('pk')])
    FormaPagamentos = tables.LinkColumn('tesouraria-details', args=[A('pk')])
    valor = tables.LinkColumn('tesouraria-details', args=[A('pk')])
    numero = tables.LinkColumn('tesouraria-details', args=[A('pk')])
    dataEmissao = tables.LinkColumn('tesouraria-details', args=[A('pk')])
    dataVencimento = tables.LinkColumn('tesouraria-details', args=[A('pk')])
    dataDisponibilidade = tables.LinkColumn('tesouraria-details', args=[A('pk')])

    class Meta:
        model = Tesouraria
        fields = ('Empresas', 'Clientes', 'Fornecedores', 'Entrada', 'Saida', 'FormaPagamentos',
                    'valor', 'numero', 'dataEmissao', 'dataVencimento', 'dataDisponibilidade')
        attrs = {"class": "table-striped table-bordered"}
        empty_text = "Não tem dados..."
