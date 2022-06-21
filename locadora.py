from veiculo import Veiculo
from locacao import Locacao
from utilitarios import pedir_confirma, pedir_inteiro, pedir_string

class Locadora:
    def __init__(self):
        self._veiculos = []
        self._locacoes = []
    
    def carrega_dados(self):
        veiculos = open('veiculos.txt')
        locacoes = open('locacoes.txt')

        veiculos.readline()
        locacoes.readline()

        for linha in veiculos:
            v = Veiculo()
            v.deserializar(linha.strip())
            self.veiculos.append(v)

        for linha in locacoes:
            l = Locacao()
            l.deserializar(linha.strip(), self.veiculos)
            self.locacoes.append(l)

        veiculos.close()
        locacoes.close()

    def consulta_veiculo(self, atributo, valor):
        sel = []

        if atributo == '1':           
            sel = [v for v in self.veiculos if v.modelo == valor.title()]
        elif atributo == '2':           
            sel = [v for v in self.veiculos if v.cor == valor.title()]
        elif atributo == '3':
            if valor.isnumeric():           
                sel = [v for v in self.veiculos if v.ano == int(valor)]
            else:
                print('Ano inválido.')
                return
        elif atributo == '4':           
            sel = [v for v in self.veiculos if v.cidade == valor.title()]

        if len([v.exibe_dados() for v in sel]) == 0:
            print(f'Nenhum carro localizado.')

    def realiza_locacao(self):
        origem = pedir_string('Informe a cidade de origem: ')

        sel = [v for v in self.veiculos if v.cidade == origem.title() and v.disponivel == True] 
        if len([v.exibe_dados() for v in sel]) == 0:
            print(f'Nenhum carro localizado.')
            return

        codigo_alugar = pedir_inteiro('\nInforme o código do veículo que deseja alugar: ')
        nome_cliente = pedir_string('Informe o nome do cliente: ')
        qt_diarias = pedir_inteiro('Informe a quantidade de diárias: ')

        sel = [l for l in self.locacoes if l.cliente == nome_cliente.title() and l.qt_dias_realizado == 0] 
        if len(sel) > 0:
            print('Cliente já possui uma locação ativa.')
        else:
            l = Locacao()
            v = l.localiza_veiculo(str(codigo_alugar), self.veiculos)

            print(f'Valor das diárias: R${v.valor_diaria * int(qt_diarias)}')
            confirma = pedir_confirma('Deseja confirmar a locação (S/N): ')

            if confirma.upper() == 'S':
                v.disponivel = False
                l.veiculo = v
                l.cliente = nome_cliente.title()
                l.origem = origem.title()
                l.destino = ''
                l.km_rodado = 0
                l.qt_dias_reserva = qt_diarias
                l.qt_dias_realizado = 0
                self.locacoes.append(l)
                self.atualiza_veiculos(v)

    def realiza_devolucao(self):
        nome_cliente = pedir_string('Informe o nome do cliente: ')
        cidade_devolucao = pedir_string('Informe a cidade de devolução: ')
        km_percorrida = pedir_inteiro('Informe a quilometragem percorrida: ')

        sel = [l for l in self.locacoes if l.cliente == nome_cliente.title() and l.qt_dias_realizado == 0] 
        if len(sel) > 0:
            print(f'Quantidade de dias contratados: {sel[0].qt_dias_reserva}')
            confirma = pedir_confirma('Utilizou uma quantidade diferente? (S/N): ')
            qt_utilizada = sel[0].qt_dias_reserva
            if confirma.upper() == 'S':
                qt_utilizada = pedir_inteiro('Quantos dias ficou com o carro: ')

            total = sel[0].valor_km_rodado(km_percorrida) + sel[0].valor_diarias(qt_utilizada)
            roaming = sel[0].valor_roaming(total, cidade_devolucao.title())
    
            print('\nValor km rodados: R${:.2f}'.format(sel[0].valor_km_rodado(km_percorrida)))
            print('Valor das diárias: R${:.2f}'.format(sel[0].valor_diarias(qt_utilizada)))
            print('Valor roaming: R${:.2f}'.format(roaming))
            print('Valor total: R${:.2f}'.format(total + roaming))

            sel[0].veiculo.odometro += km_percorrida 
            sel[0].veiculo.cidade = cidade_devolucao.title()
            sel[0].veiculo.disponivel = True
            sel[0].destino = cidade_devolucao.title()
            sel[0].qt_dias_realizado = qt_utilizada
            sel[0].km_rodado = km_percorrida

            self.atualiza_veiculos(sel[0].veiculo)
            self.atualiza_locacoes(sel[0])
        else:
            print('Cliente não possui veículo alugado.')

    def consulta_locacao(self):
        sel = []
        nome_cliente = pedir_string('Informe o nome do cliente (ENTER para não informar): ')
        modelo_veiculo = pedir_string('Informe o modelo do veículo (ENTER para não informar): ')

        if nome_cliente != '' and modelo_veiculo != '':
            sel = [l for l in self.locacoes if l.cliente == nome_cliente.title() or l.veiculo.modelo == modelo_veiculo.title()]
        elif nome_cliente != '':
            sel = [l for l in self.locacoes if l.cliente == nome_cliente.title()]
        elif modelo_veiculo != '':
            sel = [l for l in self.locacoes if l.veiculo.modelo == modelo_veiculo.title()]

        if len([l.exibe_dados() for l in sel]) == 0:
            print('Nenhuma locação encontrada.')

    def relatorio_resumo(self):
        km_rodado, qt_dias_reserva, qt_dias_realizado, valor_diarias_contratadas, valor_diarias_extras, valor_taxa_roaming, valor_km_rodados, valor_total = 0, 0, 0, 0, 0, 0, 0, 0
        sel = [l for l in self.locacoes if l.qt_dias_realizado != 0]

        for l in sel:
            total = l.valor_km_rodado(l.km_rodado) + l.valor_diarias(l.qt_dias_realizado)
            roaming = l.valor_roaming(total, l.destino)

            km_rodado += l.km_rodado 
            qt_dias_reserva += l.qt_dias_reserva
            qt_dias_realizado += l.qt_dias_realizado
            valor_diarias_contratadas += l.valor_diarias_reserva()
            valor_diarias_extras += l.valor_diarias_extra(l.qt_dias_realizado - l.qt_dias_reserva)
            valor_taxa_roaming += roaming
            valor_km_rodados += l.valor_km_rodado(l.km_rodado)
            valor_total += total + roaming

        print('\nKm rodados: {}'.format(km_rodado))
        print('Dias reservados: {}'.format(qt_dias_reserva))
        print('Dias utilizados: {}'.format(qt_dias_realizado))
        print('Valor diárias contratadas: R${:.2f}'.format(valor_diarias_contratadas))
        print('Valor diárias extra: R${:.2f}'.format(valor_diarias_extras))
        print('Valor taxa roaming: R${:.2f}'.format(valor_taxa_roaming))
        print('Valor km rodados: R${:.2f}'.format(valor_km_rodados))
        print('Valor total: R${:.2f}'.format(valor_total))

    def salva_dados(self):
        veiculos = open('veiculos.txt', 'w')
        locacoes = open('locacoes.txt', 'w')

        veiculos.write('codigo\tmodelo\tcor\tano\todometro\tcidade\tdisponivel\tvalor_diaria\tvalor_km_rodado')
        locacoes.write('veiculo\tcliente\torigem\tdestino\tkm_rodado\tqt_dias_reserva\tqt_dias_realizado')

        for v in self.veiculos:
            veiculos.write(v.serializar())

        for l in self.locacoes:
            locacoes.write(l.serializar())

        veiculos.close()
        locacoes.close()

    def atualiza_veiculos(self, veiculo):
        for v in self.veiculos:
            if v.codigo == veiculo.codigo:
                self.veiculos.remove(v)
                self.veiculos.append(veiculo)

    def atualiza_locacoes(self, locacao):
        for l in self.locacoes:
            if l.cliente == locacao.cliente:
                l = locacao

    @property
    def veiculos(self):
        return self._veiculos

    @property
    def locacoes(self):
        return self._locacoes

    @veiculos.setter
    def veiculos(self, veiculos):
        self._veiculos = veiculos

    @locacoes.setter
    def locacoes(self, locacoes):
        self._locacoes = locacoes
