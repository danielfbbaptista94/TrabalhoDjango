from django.shortcuts import render
from django.views.generic import CreateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django_tables2 import RequestConfig
from .models import (
    Clientes, Empresas, Fornecedores,
    FormaPagamentos, ContasBancarias,
    PlanoContas, LancamentosReceber,
    LancamentosPagar, BaixasReceber,
    BaixasPagar, Tesouraria
)
from .tables import (
    LancamentosReceberTable, LancamentosPagarTable,
    BaixasReceberTable, BaixasPagarTable,
    TesourariaTable
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


class LancamentosReceberListView(LoginRequiredMixin, ListView):
    model = LancamentosReceber
    template_name = 'lancamentosreceber_list.html'
    context_object_name = 'lancamentosreceber'

    def get_context_data(self, **kwargs):
        context = super(LancamentosReceberListView, self).get_context_data(**kwargs)
        context['nav_lancamentosreceber'] = True
        table = LancamentosReceberTable(LancamentosReceber.objects.all())
        RequestConfig(self.request, paginate={'per_page': 30}).configure(table)
        context['table'] = table
        return context


class LancamentosPagarCreateView(LoginRequiredMixin, CreateView):
    model = LancamentosPagar
    success_url = '/'
    fields = ['Fornecedores', 'empresa', 'dataVencimento', 'dataEmissao', 'numeroDocumento', 'valorTitulo']

    def form_valid(self, form):
        return super().form_valid(form)


class LancamentosPagarListViw(LoginRequiredMixin, ListView):
    model = LancamentosPagar
    template_name = 'lancamentospagar_list.html'
    context_object_name = 'lancamentospagar'

    def get_context_data(self, **kwargs):
        context = super(LancamentosPagarListViw, self).get_context_data(**kwargs)
        context['nav_lancamentosreceber'] = True
        table = LancamentosPagarTable(LancamentosPagar.objects.all())
        RequestConfig(self.request, paginate={'per_page': 30}).configure(table)
        context['table'] = table
        return context


class BaixasReceberCreateView(LoginRequiredMixin, CreateView):
    model = BaixasReceber
    success_url = '/'
    fields = ['empresa', 'FormaPagamento', 'CaixaBanco', 'vencimentoPagamento', 'disponibilidade',
              'dataBaixa', 'numeroDocumento', 'valorRecebido', 'valorResidual']

    def form_valid(self, form):
        return super().form_valid(form)


class BaixasReceberListView(LoginRequiredMixin, ListView):
    model = BaixasReceber
    template_name = 'baixasreceber_list.html'
    context_object_name = 'baixasreceber'

    def get_context_data(self, **kwargs):
        context = super(BaixasReceberListView, self).get_context_data(**kwargs)
        context['nav_lancamentosreceber'] = True
        table = BaixasReceberTable(BaixasReceber.objects.all())
        RequestConfig(self.request, paginate={'per_page': 30}).configure(table)
        context['table'] = table
        return context


class BaixasPagarCreateView(LoginRequiredMixin, CreateView):
    model = BaixasPagar
    success_url = '/'
    fields = ['Empresa', 'FormaPagamento', 'CaixaBanco', 'VencimentoPagamento', 'Disponibilidade',
              'DataBaixa', 'NumeroDocumento', 'ValorRecebido', 'ValorResidual']

    def form_valid(self, form):
        return super().form_valid(form)


class BaixasPagarListView(LoginRequiredMixin, ListView):
    model = BaixasPagar
    template_name = 'baixaspagar_list.html'
    context_object_name = 'baixaspagar'

    def get_context_data(self, **kwargs):
        context = super(BaixasPagarListView, self).get_context_data(**kwargs)
        context['nav_lancamentosreceber'] = True
        table = BaixasPagarTable(BaixasPagar.objects.all())
        RequestConfig(self.request, paginate={'per_page': 30}).configure(table)
        context['table'] = table
        return context


class TesourariaCreateView(LoginRequiredMixin, CreateView):
    model = Tesouraria
    success_url = '/'
    fields = ['Empresas', 'Clientes', 'Fornecedores', 'Entrada', 'Saida', 'FormaPagamentos',
              'valor', 'numero', 'dataEmissao', 'dataVencimento', 'dataDisponibilidade']

    def form_valid(self, form):
        return super().form_valid(form)


class TesourariaListView(LoginRequiredMixin, ListView):
    model = Tesouraria
    template_name = 'tesouraria_list.html'
    context_object_name = 'tesouraria'

    def get_context_data(self, **kwargs):
        context = super(TesourariaListView, self).get_context_data(**kwargs)
        context['nav_lancamentosreceber'] = True
        table = TesourariaTable(Tesouraria.objects.all())
        RequestConfig(self.request, paginate={'per_page': 30}).configure(table)
        context['table'] = table
        return context
