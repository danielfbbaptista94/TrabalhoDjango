from django.shortcuts import render
from django.views.generic import CreateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import (
    Clientes, Empresas, Fornecedores,
    FormaPagamentos, ContasBancarias,
    PlanoContas, LancamentosReceber,
    LancamentosPagar, BaixasReceber,
    BaixasPagar, Tesouraria
)


def home(request):
    return render(request, 'financeiro/home.html')


class ClienteCreateView(LoginRequiredMixin, CreateView):
    model = Clientes
    success_url = '/'
    fields = ['razaoSocial', 'identificacao', 'tipoPessoa', 'cnpjCpf', 'inscricaoEstadual', 'inscricaoMunicipal',
              'endereco', 'bairro', 'municipio', 'cep', 'uf', 'telefone', 'email', 'nome_titular', 'cpf', 'funcao']

    def form_valid(self, form):
        return super().form_valid(form)


class EmpresaCreateView(LoginRequiredMixin, CreateView):
    model = Empresas
    success_url = '/'
    fields = ['razaoSocial', 'identificacao', 'tipoPessoa', 'cnpj', 'inscricaoEstadual', 'inscricaoMunicipal',
              'endereco', 'bairro', 'municipio', 'cep', 'uf', 'telefone', 'email', 'nome_titular', 'cpf', 'funcao']

    def form_valid(self, form):
        return super().form_valid(form)


class FornecedorCreateView(LoginRequiredMixin, CreateView):
    model = Fornecedores
    success_url = '/'
    fields = ['razaoSocial', 'identificacao', 'tipoPessoa', 'cnpjCpf', 'inscricaoEstadual', 'inscricaoMunicipal',
              'endereco', 'bairro', 'municipio', 'cep', 'uf', 'telefone', 'email', 'nome_titular', 'cpf', 'funcao']

    def form_valid(self, form):
        return super().form_valid(form)


class FormaPagamentoCreateView(LoginRequiredMixin, CreateView):
    model = FormaPagamentos
    success_url = '/'
    fields = ['descricao']

    def form_valid(self, form):
        return super().form_valid(form)


class ContasBancariasCreateView(LoginRequiredMixin, CreateView):
    model = ContasBancarias
    success_url = '/'
    fields = ['classificacao', 'descricao', 'numeroConta', 'numeroAgencia',
                'dataSaldoInicial', 'saldoInicial', 'tipo']

    def form_valid(self, form):
        return super().form_valid(form)


class PlanoContasCreateView(LoginRequiredMixin, CreateView):
    model = PlanoContas
    success_url = '/'
    fields = ['conta', 'classificacao', 'descricao', 'tipo', 'caracteristica']

    def form_valid(self, form):
        return super().form_valid(form)


class LancamentosReceberCreateView(LoginRequiredMixin, CreateView):
    model = LancamentosReceber
    success_url = '/'
    fields = ['cliente', 'empresa', 'dataVencimento', 'dataEmissao', 'numeroDocumento', 'valorTitulo']

    def form_valid(self, form):
        return super().form_valid(form)


class LancamentosPagarCreateView(LoginRequiredMixin, CreateView):
    model = LancamentosPagar
    success_url = '/'
    fields = ['Fornecedores', 'Empresas', 'dataVencimento', 'dataEmissao', 'numeroDocumento', 'valorTitulo']

    def form_valid(self, form):
        return super().form_valid(form)


class BaixasReceberCreateView(LoginRequiredMixin, CreateView):
    model = BaixasReceber
    success_url = '/'
    fields = ['empresa', 'caixaBanco', 'vencimentoPagamento', 'disponibilidade',
              'dataBaixa', 'numeroDocumento', 'valorRecebido', 'valorResidual']

    def form_valid(self, form):
        return super().form_valid(form)


class BaixasPagarCreateView(LoginRequiredMixin, CreateView):
    model = BaixasPagar
    success_url = '/'
    fields = ['empresa', 'caixaBanco', 'vencimentoPagamento', 'disponibilidade',
              'dataBaixa', 'numeroDocumento', 'valorRecebido', 'valorResidual']

    def form_valid(self, form):
        return super().form_valid(form)


class TesourariaCreateView(LoginRequiredMixin, CreateView):
    model = Tesouraria
    success_url = '/'
    fields = ['Empresas', 'Clientes', 'PlanoContas', 'FormaPagamentos', 'Fornecedores',
              'valor', 'numero', 'datEmissao', 'dataVencimento', 'dataDisponibilidade']

    def form_valid(self, form):
        return super().form_valid(form)
