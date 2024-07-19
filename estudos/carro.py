class Carro:
    def __init__(self, ano = '', modelo = '' , cor = ''):
        pass
        self.ano = ano
        self.modelo = modelo
        self.cor = cor
    
    def __str__(self):
        pass
        return f'{self.ano} | {self.modelo} | {self.cor}'
    
  

fiatToro = Carro('2024', 'fiat toro', 'preto')

if fiatToro.cor == 'prata':
    print('carro é prata')
else:
    print('cliente nao quer carro que n é prata')
