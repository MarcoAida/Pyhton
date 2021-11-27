class NumericalCSVFile():

    def __init__(self, name):
        self.name = name
        my_file = open(self.name, 'r')
        
    def get_data(self):
        my_file = open(self.name, 'r')
        my_list = []

        for line in my_file:
            element = line.split(',')
            element[1] = element[1].strip()

            if element [0] != 'Date':
                value = element [1]

                try:
                    my_list.append(float(value))

                except ValueError:
                    print('Non posso convertire un simbolo a valore numerico !!')
                    print('Ho avuto un errore di Valore. "values" ere un simbolo.')

                except TypeError:
                    print('Non posso convertire un simbolo a valore numerico !!')
                    print('Ho avuto un errore di Tipo. "values" ere un simbolo.')
                    
                except Exception as e:
                    print('Non ho trovato il file.. {}' .format(e))

                my_list.append(element)

        return(my_list)

shampooFile = NumericalCSVFile('shampoo_parte2.txt')
shampoo = shampooFile.get_data()

print(shampoo)