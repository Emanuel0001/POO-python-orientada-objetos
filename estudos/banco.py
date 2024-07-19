class BancoNubank:
    
    def __init__(self, titular = '', saldo = 0):
        self.titular = titular.upper()
        self.saldo = saldo
        self._ativo = False
    
    def __str__(self):
        status = 'Ativo' if self._ativo else 'Desativado'
        return f'Olá, Sr(a) {self.titular} seu saldo bancário é {self.formatar_saldo()}, status do cliente: {status}'
    
    def formatar_saldo(self):
        return '{:,.2f}'.format(self.saldo).replace('.', ',')
    
    def status_cliente(self):
        return 'Ativo' if self._ativo else 'Desativado'

    def ativa_cliente(self):
         self._ativo = True

cliente = BancoNubank('Emanuel',10000)

print(cliente)