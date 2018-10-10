# Generated by Django 2.1.2 on 2018-10-09 22:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('financeiro', '0006_auto_20181009_1908'),
    ]

    operations = [
        migrations.AlterField(
            model_name='baixaspagar',
            name='DataBaixa',
            field=models.DateField(default=datetime.datetime(2018, 10, 9, 19, 12, 32, 541276)),
        ),
        migrations.AlterField(
            model_name='baixaspagar',
            name='Disponibilidade',
            field=models.DateField(default=datetime.datetime(2018, 10, 9, 19, 12, 32, 541276)),
        ),
        migrations.AlterField(
            model_name='baixaspagar',
            name='VencimentoPagamento',
            field=models.DateField(default=datetime.datetime(2018, 10, 9, 19, 12, 32, 541276)),
        ),
        migrations.AlterField(
            model_name='baixasreceber',
            name='dataBaixa',
            field=models.DateField(default=datetime.datetime(2018, 10, 9, 19, 12, 32, 541276)),
        ),
        migrations.AlterField(
            model_name='baixasreceber',
            name='disponibilidade',
            field=models.DateField(default=datetime.datetime(2018, 10, 9, 19, 12, 32, 541276)),
        ),
        migrations.AlterField(
            model_name='baixasreceber',
            name='vencimentoPagamento',
            field=models.DateField(default=datetime.datetime(2018, 10, 9, 19, 12, 32, 541276)),
        ),
        migrations.AlterField(
            model_name='contasbancarias',
            name='dataSaldoInicial',
            field=models.DateField(default=datetime.datetime(2018, 10, 9, 19, 12, 32, 541276)),
        ),
        migrations.AlterField(
            model_name='lancamentospagar',
            name='dataEmissao',
            field=models.DateField(default=datetime.datetime(2018, 10, 9, 19, 12, 32, 541276)),
        ),
        migrations.AlterField(
            model_name='lancamentospagar',
            name='dataVencimento',
            field=models.DateField(default=datetime.datetime(2018, 10, 9, 19, 12, 32, 541276)),
        ),
        migrations.AlterField(
            model_name='lancamentosreceber',
            name='dataEmissao',
            field=models.DateField(default=datetime.datetime(2018, 10, 9, 19, 12, 32, 541276)),
        ),
        migrations.AlterField(
            model_name='lancamentosreceber',
            name='dataVencimento',
            field=models.DateField(default=datetime.datetime(2018, 10, 9, 19, 12, 32, 541276)),
        ),
        migrations.AlterField(
            model_name='tesouraria',
            name='dataDisponibilidade',
            field=models.DateField(default=datetime.datetime(2018, 10, 9, 19, 12, 32, 545270)),
        ),
        migrations.AlterField(
            model_name='tesouraria',
            name='dataEmissao',
            field=models.DateField(default=datetime.datetime(2018, 10, 9, 19, 12, 32, 545270)),
        ),
        migrations.AlterField(
            model_name='tesouraria',
            name='dataVencimento',
            field=models.DateField(default=datetime.datetime(2018, 10, 9, 19, 12, 32, 545270)),
        ),
    ]
