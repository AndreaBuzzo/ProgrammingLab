mia_lista = [4, 6, 8, 98, 43, 11]

def somma_lista(mia_lista_input):
    risultato = 0
    for i in mia_lista:
        risultato = risultato + i
    return risultato

somma = somma_lista(mia_lista)
print('Risultato: {}'.format(somma))
      