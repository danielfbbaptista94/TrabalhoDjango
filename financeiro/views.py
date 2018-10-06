from django.shortcuts import render


def home(request):
    return render(request, 'financeiro/home.html')


def cliente(request):
    return render(request, 'financeiro/cliente.html')


def empresa(request):
    return render(request, 'financeiro/empresa.html')


def fornecedor(request):
    return render(request, 'financeiro/fornecedor.html')
