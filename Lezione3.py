mio_file = open('vendite.csv', 'r')

def somma_vendite(mia_lista_input):

    somma = 0.

    for line in mia_lista_input:

        elementi = line.split(',')

        if elementi[0] != 'Date':
            data = elementi[0]
            valore = elementi[1]
            valore = float(valore)
    
            somma = somma + valore
    
    return somma

somma = somma_vendite(mio_file)
print('Risultato: {}'.format(somma))

mio_file.close()

