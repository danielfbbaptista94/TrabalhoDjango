from django.urls import path
from . import views
from .views import (
    ClienteCreateView,
    EmpresaCreateView,
    FornecedorCreateView,
    FormaPagamentoCreateView,
    ContasBancariasCreateView,
    PlanoContasCreateView,
    LancamentosReceberCreateView,
    LancamentosPagarCreateView,
    BaixasReceberCreateView,
    BaixasPagarCreateView,
    TesourariaCreateView,
    LancamentosPagarListViw,
    LancamentosReceberListView,
    BaixasReceberListView,
    BaixasPagarListView,
    TesourariaListView,
)


urlpatterns = [
    path('', views.home, name='financeiro-home'),
    path('cliente/new/', ClienteCreateView.as_view(), name='clientes-create'),
    path('empresa/new/', EmpresaCreateView.as_view(), name='empresas-create'),
    path('fornecedor/new/', FornecedorCreateView.as_view(), name='fornecedores-create'),
    path('formaPagamento/new/', FormaPagamentoCreateView.as_view(), name='formapagamentos-create'),
    path('contaBancaria/new/', ContasBancariasCreateView.as_view(), name='contasbancarias-create'),
    path('planoConta/new/', PlanoContasCreateView.as_view(), name='planocontas-create'),
    path('lancamentosReceber/new/', LancamentosReceberCreateView.as_view(), name='lancamentosreceber-create'),
    path('lancamentosReceber/details/', LancamentosReceberListView.as_view(), name='lancamentosreceber-details'),
    path('lancamentosPagar/new/', LancamentosPagarCreateView.as_view(), name='lancamentospagar-create'),
    path('lancamentosPagar/details/', LancamentosPagarListViw.as_view(), name='lancamentospagar-details'),
    path('baixasReceber/new/', BaixasReceberCreateView.as_view(), name='baixasreceber-create'),
    path('baixasReceber/details/', BaixasReceberListView.as_view(), name='baixasreceber-details'),
    path('baixasPagar/new/', BaixasPagarCreateView.as_view(), name='baixaspagar-create'),
    path('baixasPagar/details/', BaixasPagarListView.as_view(), name='baixaspagar-details'),
    path('tesouraria/new/', TesourariaCreateView.as_view(), name='tesouraria-create'),
    path('tesouraria/details/', TesourariaListView.as_view(), name='tesouraria-details'),
]
