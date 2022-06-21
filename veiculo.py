class Veiculo:
    def __init__(self, codigo=None, modelo=None, cor=None, ano=None, odometro=None, cidade=None, disponivel=None, valor_diaria=None, valor_km_rodado=None):
        self._codigo = codigo
        self._modelo = modelo
        self._cor = cor
        self._ano = ano
        self._odometro = odometro
        self._cidade = cidade
        self._disponivel = disponivel
        self._valor_diaria = valor_diaria
        self._valor_km_rodado = valor_km_rodado

    def deserializar(self, linha):
        dados = linha.split('\t')
        self.codigo = dados[0]
        self.modelo = dados[1]
        self.cor = dados[2]
        self.ano = int(dados[3])
        self.odometro = int(dados[4])
        self.cidade = dados[5]
        self.disponivel = True if dados[6] == 'S' else False
        self.valor_diaria = float(dados[7])
        self.valor_km_rodado = float(dados[8])

    def serializar(self):
        disponivel = 'S' if self.disponivel else 'N'
        return f'\n{self.codigo}\t{self.modelo}\t{self.cor}\t{self.ano}\t{self.odometro}\t{self.cidade}\t{disponivel}\t{self.valor_diaria}\t{self.valor_km_rodado}'

    def exibe_dados(self):
        print(f'\nCódigo: {self.codigo}')
        print(f'Modelo: {self.modelo}')
        print(f'Cor: {self.cor}')
        print(f'Ano: {self.ano}')
        print(f'Odômetro: {self.odometro}km')
        print(f'Cidade: {self.cidade}')
        print('Disponível: {}'.format('Sim' if self.disponivel else 'Não'))
        print(f'Valor da diária: R${self.valor_diaria}')
        print(f'Valor km rodado: R${self.valor_km_rodado}')

    # def adicionar_veiculo():
    #     modelo = input('Informe o modelo do veículo: ')
    #     cor = input('Informe a cor do veículo: ')
    #     ano = input('Informe o ano do veículo: ')
    #     odometro = input('Informe o odometro do veículo: ')
    #     valor_diaria = input('Informe o valor da diaria: ')
    #     valor_km_rodado = input('Informe o valor por km rodado: ')

    @property
    def codigo(self):
        return self._codigo

    @codigo.setter
    def codigo(self, codigo):
        self._codigo = codigo

    @property
    def modelo(self):
        return self._modelo

    @modelo.setter
    def modelo(self, modelo):
        self._modelo = modelo

    @property
    def cor(self):
        return self._cor

    @cor.setter
    def cor(self, cor):
        self._cor = cor

    @property
    def ano(self):
        return self._ano

    @ano.setter
    def ano(self, ano):
        self._ano = ano

    @property
    def odometro(self):
        return self._odometro

    @odometro.setter
    def odometro(self, odometro):
        self._odometro = odometro

    @property
    def cidade(self):
        return self._cidade

    @cidade.setter
    def cidade(self, cidade):
        self._cidade = cidade

    @property
    def disponivel(self):
        return self._disponivel

    @disponivel.setter
    def disponivel(self, disponivel):
        self._disponivel = disponivel

    @property
    def valor_diaria(self):
        return self._valor_diaria

    @valor_diaria.setter
    def valor_diaria(self, valor_diaria):
        self._valor_diaria = valor_diaria

    @property
    def valor_km_rodado(self):
        return self._valor_km_rodado

    @valor_km_rodado.setter
    def valor_km_rodado(self, valor_km_rodado):
        self._valor_km_rodado = valor_km_rodado
