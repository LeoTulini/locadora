import os
from utilitarios import *
from locadora import Locadora

verifica_cabecalho()
locadora = Locadora()
locadora.carrega_dados()

def exibir_menu():
    os.system('cls')
    print('1 - Consultar veículo')
    print('2 - Realizar locação')
    print('3 - Realizar devolução')
    print('4 - Consultar locações')
    print('5 - Resumo')
    print('6 - Salvar')
    print('7 - Sair')

def consultar_veiculo():
    os.system('cls')
    print('1 - Modelo')
    print('2 - Cor')
    print('3 - Ano')
    print('4 - Cidade')

    atributo = input('\nDeseja buscar por qual atributo: ')
    valor = input('Informe o valor: ')

    os.system('cls')
    locadora.consulta_veiculo(atributo, valor)

if __name__ == '__main__':
    escolha = ''

    while escolha != '7':
        exibir_menu()
        escolha = input('\nEscolha uma opção: ')
        os.system('cls')

        if escolha == '1':
            consultar_veiculo()
        elif escolha == '2':
            locadora.realiza_locacao()
        elif escolha == '3':
            locadora.realiza_devolucao()
        elif escolha == '4':
            locadora.consulta_locacao()
        elif escolha == '5':
            locadora.relatorio_resumo()
        elif escolha == '6':
            locadora.salva_dados()
            print('Dados salvos com sucesso!')
        elif escolha == '7':
            locadora.salva_dados()
            print('Saindo...\n')
        else:
            print('Opção inválida!')
        
        if escolha != '7':
            pedir_string('\nPressione ENTER para continuar...')
