from django.contrib import admin
from .models import *


admin.site.register(Clientes)
admin.site.register(Empresas)
admin.site.register(Fornecedores)
admin.site.register(FormaPagamentos)
admin.site.register(ContasBancarias)
admin.site.register(PlanoContas)
admin.site.register(LancamentosReceber)
admin.site.register(LancamentosPagar)
admin.site.register(BaixasReceber)
admin.site.register(BaixasPagar)
admin.site.register(Tesouraria)
