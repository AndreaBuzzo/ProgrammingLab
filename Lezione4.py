class CSVFile():
    def __init__(self, name):
        self.name = name
    
    def get_data(self):
        elements = 0
        somma = ''
        my_file = open(self.name, 'r')
        for line in my_file:
            element = line.split(',')
            if element[0] != 'Date':
                data = element[0]
                valore = element[1]
                elements = data + valore
                somma = somma + elements
        my_file.close()
        return somma
        

csv = CSVFile('vendite.csv')
print('csv')
print(csv.get_data())

