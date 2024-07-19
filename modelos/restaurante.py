from modelos.avaliacao import Avaliacao

class Restaurante:
    """representa um restaurante e suas caracteristicas"""

    restaurantes = []
    def __init__(self, nome, categoria):
         
        """  Inicializa uma instância de Restaurante.

        Parâmetros:
        - nome (str): O nome do restaurante.
        - categoria (str): A categoria do restaurante.
      """
         
        self.nome = nome.title()
        self.categoria = categoria.upper()
        self._ativo = False
        self._avaliacao = []
        Restaurante.restaurantes.append(self)
        
    def __str__(self):
        """Retorna uma representação em string do restaurante."""
        return f'{self.nome} | {self.categoria}'
    
    print(f'{"Nome".ljust(20)} | {"Categoria".ljust(20)} | {"Ativo".ljust(20)} | {"Avaliação"}')
   
    @classmethod
    def listar_restaurantes(cls):
        """Exibe uma lista formatada de todos os restaurantes."""
        for resturante in cls.restaurantes:
            print(f'{resturante.nome.ljust(20)} | {resturante.categoria.ljust(20)} | {resturante.ativo.ljust(20)} | {resturante.media_avaliacao}')

    @property
    def ativo(self):
        """Retorna um símbolo indicando o estado de atividade do restaurante."""
        return '⌧' if self._ativo else '☐'  # Use _ativo here
    
    def alternar_estado(self):
        """ alterna o estado do estaurante se tiver ativo fica inativo ou contrário"""
        self._ativo = not self._ativo
    
    def receber_avaliacao(self, cliente, nota):
        """ funcao para pegas as avaliações do clientes"""
        pass
        if  0 < nota <= 5:
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacao.append(avaliacao)
        
    @property
    def media_avaliacao(self):
        """ calcula a media das avaliações do restaurante"""
        if not self._avaliacao:
            return '-'
        somas_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        qtd_notas = len(self._avaliacao)
        media = round(somas_das_notas / qtd_notas, 1)
        return media
    
# restaurante_praca = Restaurante('preca','Fast')
# restaurante_praca.alternar_estado()
# restaurante_pizza = Restaurante('pizza','italiana')
# restaurante_dell = Restaurante('japones','shushi', )
Restaurante.listar_restaurantes()
