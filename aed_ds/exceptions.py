class EmptyListException(Exception):
    print('Nao existem elementos na lista.')

class InvalidPositionException(Exception):
    print('Posicao invalida.')

class NoSuchElementException(Exception):
    print('Nao existe o elemento pedido.')
    