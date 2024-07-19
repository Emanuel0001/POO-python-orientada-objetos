from modelos.restaurante import Restaurante

restaurante_praca = Restaurante('Praça', 'Gourmet')
restaurante_praca.receber_avaliacao('emanuel hitallo', 4)
restaurante_praca.receber_avaliacao('emanuel ', 7)

def main():
    pass
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()