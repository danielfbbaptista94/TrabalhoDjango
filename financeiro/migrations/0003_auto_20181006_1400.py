# Generated by Django 2.1.2 on 2018-10-06 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('financeiro', '0002_auto_20181003_2006'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lancamentospagar',
            old_name='fk_Empresas',
            new_name='Empresas',
        ),
        migrations.RenameField(
            model_name='lancamentospagar',
            old_name='fk_Fornecedores',
            new_name='Fornecedores',
        ),
        migrations.RenameField(
            model_name='lancamentosreceber',
            old_name='Clientes',
            new_name='cliente',
        ),
        migrations.RenameField(
            model_name='lancamentosreceber',
            old_name='datEmissao',
            new_name='dataEmissao',
        ),
        migrations.RenameField(
            model_name='lancamentosreceber',
            old_name='Empresas',
            new_name='empresa',
        ),
        migrations.RenameField(
            model_name='tesouraria',
            old_name='fk_Clientes',
            new_name='Clientes',
        ),
        migrations.RenameField(
            model_name='tesouraria',
            old_name='fk_Empresas',
            new_name='Empresas',
        ),
        migrations.RenameField(
            model_name='tesouraria',
            old_name='fk_FormaPagamentos',
            new_name='FormaPagamentos',
        ),
        migrations.RenameField(
            model_name='tesouraria',
            old_name='fk_Fornecedores',
            new_name='Fornecedores',
        ),
        migrations.RenameField(
            model_name='tesouraria',
            old_name='fk_PlanoContas',
            new_name='PlanoContas',
        ),
        migrations.AlterField(
            model_name='lancamentosreceber',
            name='numeroDocumento',
            field=models.CharField(max_length=5),
        ),
    ]
