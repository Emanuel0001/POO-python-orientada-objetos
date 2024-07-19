class Pessoa:
    pass
    def __init__ (self, nome = '', idade = 0, profisssao = ''):
        pass
        self.nome = nome
        self.idade = idade
        self.profisssao = profisssao
    
    def __str__(self):
        pass
        return f'Nome: {self.nome} | Idade: {self.idade} | Profissão: {self.profisssao}'
    
    def aniversario(self):
        self.idade += 1

    def saudacao(self):
        try:
            if self.profisssao == 'software engineer':
                print('Saudações web development')
            elif self.profisssao == 'professor':
                print('Saudações teacher')
            elif self.profisssao == 'enfermeiro':
                print('Saldações nurse')
            else:
                print('saudações desempregado')
        except:
              print('voce é um ze ninguem')


pessoa = Pessoa('hitallo', 26, 'software engineer')
pessoa.aniversario()
pessoa.saudacao()

pessoa2 = Pessoa('marivania', 43, 'professor')
pessoa2.saudacao()

pessoa3 = Pessoa('lula', 43, 'carteira de trabalho')
pessoa3.saudacao()
print(pessoa)
print(pessoa2)