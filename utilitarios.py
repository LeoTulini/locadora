msg_erro = 'Entrada inválida.'

def pedir_inteiro(msg):
    while True:
        try:
            return int(input(msg))
        except:
            print(msg_erro)

def pedir_float(msg):
    while True:
        try:
            return float(input(msg))
        except:
            print(msg_erro)

def pedir_string(msg):
    valor = input(msg)
    while valor.isdigit() == True:
        print(msg_erro)
        valor = input(msg)
    return valor

def pedir_confirma(msg):
    valor = input(msg)
    while valor not in 'SsNn':
        print(msg_erro)
        valor = input(msg)
    return valor

def verifica_cabecalho():
    locacoes = open('locacoes.txt', 'a')
    veiculos = open('veiculos.txt', 'a')

    if locacoes.tell() == 0:
        locacoes.write('veiculo\tcliente\torigem\tdestino\tkm_rodado\tqt_dias_reserva\tqt_dias_realizado')

    if veiculos.tell() == 0:
        veiculos.write('codigo\tmodelo\tcor\tano\todometro\tcidade\tdisponivel\tvalor_diaria\tvalor_km_rodado')

    locacoes.close
    veiculos.close
