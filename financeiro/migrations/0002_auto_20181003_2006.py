# Generated by Django 2.1.2 on 2018-10-03 23:06

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('financeiro', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BaixasPagar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vencimentoPagamento', models.DateField(default=datetime.date.today)),
                ('disponibilidade', models.DateField(default=datetime.date.today)),
                ('dataBaixa', models.DateField(default=datetime.date.today)),
                ('numeroDocumento', models.CharField(max_length=5)),
                ('valorRecebido', models.FloatField(max_length=5)),
                ('valorResidual', models.FloatField(max_length=5)),
                ('caixaBanco', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='financeiro.FormaPagamentos')),
            ],
            options={
                'verbose_name_plural': 'Baixa de Conta a Pagar',
            },
        ),
        migrations.CreateModel(
            name='BaixasReceber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vencimentoPagamento', models.DateField(default=datetime.date.today)),
                ('disponibilidade', models.DateField(default=datetime.date.today)),
                ('dataBaixa', models.DateField(default=datetime.date.today)),
                ('numeroDocumento', models.CharField(max_length=5)),
                ('valorRecebido', models.FloatField(max_length=5)),
                ('valorResidual', models.FloatField(max_length=5)),
                ('caixaBanco', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='financeiro.FormaPagamentos')),
            ],
            options={
                'verbose_name_plural': 'Baixa de Conta a Receber',
            },
        ),
        migrations.CreateModel(
            name='LancamentosPagar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dataVencimento', models.DateField(default=datetime.date.today)),
                ('datEmissao', models.DateField(default=datetime.date.today)),
                ('valorTitulo', models.FloatField(max_length=5)),
                ('numeroDocumento', models.IntegerField()),
                ('fk_Empresas', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='financeiro.Empresas')),
                ('fk_Fornecedores', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='financeiro.Fornecedores')),
            ],
            options={
                'verbose_name_plural': 'Lancamentos a Pagar',
            },
        ),
        migrations.CreateModel(
            name='LancamentosReceber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dataVencimento', models.DateField(default=datetime.date.today)),
                ('datEmissao', models.DateField(default=datetime.date.today)),
                ('valorTitulo', models.FloatField(max_length=5)),
                ('numeroDocumento', models.IntegerField()),
                ('Clientes', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='financeiro.Clientes')),
                ('Empresas', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='financeiro.Empresas')),
            ],
            options={
                'verbose_name_plural': 'Lancamentos a Receber',
            },
        ),
        migrations.CreateModel(
            name='Tesouraria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.FloatField(max_length=5)),
                ('numero', models.IntegerField()),
                ('datEmissao', models.DateField(default=datetime.date.today)),
                ('dataVencimento', models.DateField(default=datetime.date.today)),
                ('dataDisponibilidade', models.DateField(default=datetime.date.today)),
                ('fk_Clientes', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='financeiro.Clientes')),
                ('fk_Empresas', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='financeiro.Empresas')),
                ('fk_FormaPagamentos', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='financeiro.FormaPagamentos')),
                ('fk_Fornecedores', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='financeiro.Fornecedores')),
                ('fk_PlanoContas', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='financeiro.PlanoContas')),
            ],
            options={
                'verbose_name_plural': 'Tesouraria',
            },
        ),
        migrations.AddField(
            model_name='contasbancarias',
            name='dataSaldoInicial',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='baixasreceber',
            name='empresa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='financeiro.LancamentosReceber'),
        ),
        migrations.AddField(
            model_name='baixaspagar',
            name='empresa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='financeiro.LancamentosPagar'),
        ),
    ]