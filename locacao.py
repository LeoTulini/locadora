from veiculo import Veiculo

class Locacao:
    def __init__(self, veiculo=None, cliente=None, origem=None, destino=None, km_rodados=None, qt_dias_reserva=None, qt_dias_realizado=None):
        self._veiculo = veiculo
        self._cliente = cliente
        self._origem = origem
        self._destino = destino
        self._km_rodado = km_rodados
        self._qt_dias_reserva = qt_dias_reserva
        self._qt_dias_realizado = qt_dias_realizado

    def deserializar(self, linha, veiculos):
        dados = linha.split('\t')
        v = self.localiza_veiculo(dados[0], veiculos)

        self.veiculo = Veiculo(v.codigo, v.modelo, v.cor, v.ano, v.odometro, v.cidade, v.disponivel, v.valor_diaria, v.valor_km_rodado)
        self.cliente = dados[1]
        self.origem = dados[2]
        self.destino = dados[3]
        self.km_rodado = 0 if dados[4] == '' else int(dados[4])
        self.qt_dias_reserva = int(dados[5])
        self.qt_dias_realizado = 0 if len(dados) == 6 else int(dados[6])

    def serializar(self):
        km_rodado = '' if self.km_rodado == 0 else self.km_rodado
        qt_dias_realizado = '' if self.qt_dias_realizado == 0 else self.qt_dias_realizado
        return f'\n{self.veiculo.codigo}\t{self.cliente}\t{self.origem}\t{self.destino}\t{km_rodado}\t{self.qt_dias_reserva}\t{qt_dias_realizado}'

    def valor_diarias(self, qt_utilizada):
        return self.valor_diarias_reserva() + self.valor_diarias_extra(qt_utilizada) 

    def valor_diarias_extra(self, qt_utilizada):
        diferenca_dias = qt_utilizada - self.qt_dias_reserva
        valor_diarias_extra = diferenca_dias * self.veiculo.valor_diaria

        if qt_utilizada < self.qt_dias_reserva:
            return (self.veiculo.valor_diaria * 0.2) * diferenca_dias
        elif qt_utilizada > self.qt_dias_reserva:
            return (self.veiculo.valor_diaria * 0.3) * diferenca_dias

        return valor_diarias_extra

    def valor_diarias_reserva(self):
         return self.veiculo.valor_diaria * self.qt_dias_reserva

    def valor_roaming(self, valor, cidade_devolucao):
        if self.origem != cidade_devolucao:
            return valor * 0.15
        return 0

    def valor_km_rodado(self, km_percorrida):
        return self.veiculo.valor_km_rodado * km_percorrida

    def localiza_veiculo(self, codigo, veiculos):
        for veiculo in veiculos:
            if veiculo.codigo == codigo:
                return veiculo
        return None

    def exibe_dados(self):
        self.veiculo.exibe_dados()
        print('------------------------')
        print(f'Cliente: {self.cliente}')
        print(f'Origem: {self.origem}')
        print(f'Destino: {self.destino}')
        print(f'Km rodados: {self.km_rodado}')
        print(f'Dias reservados: {self.qt_dias_reserva}')
        print(f'Dias utilizados: {self.qt_dias_realizado}')  

    @property
    def veiculo(self):
        return self._veiculo

    @veiculo.setter
    def veiculo(self, veiculo):
        self._veiculo = veiculo

    @property
    def cliente(self):
        return self._cliente

    @cliente.setter
    def cliente(self, cliente):
        self._cliente = cliente

    @property
    def origem(self):
        return self._origem

    @origem.setter
    def origem(self, origem):
        self._origem = origem

    @property
    def destino(self):
        return self._destino

    @destino.setter
    def destino(self, destino):
        self._destino = destino

    @property
    def km_rodado(self):
        return self._km_rodado

    @km_rodado.setter
    def km_rodado(self, km_rodado):
        self._km_rodado = km_rodado

    @property
    def qt_dias_reserva(self):
        return self._qt_dias_reserva

    @qt_dias_reserva.setter
    def qt_dias_reserva(self, qt_dias_reserva):
        self._qt_dias_reserva = qt_dias_reserva

    @property
    def qt_dias_realizado(self):
        return self._qt_dias_realizado

    @qt_dias_realizado.setter
    def qt_dias_realizado(self, qt_dias_realizado):
        self._qt_dias_realizado = qt_dias_realizado
