class NumericalCSVFile():

    def __init__(self, name):
        self.name = name
        my_file = open(self.name, 'r')
        
    def get_data(self):
        my_file = open(self.name, 'r')
        my_list = []
        values = []

        for line in my_file:
            element = line.split(',')
            element[1] = element[1].strip()

            if element [0] != 'Date':
                value = element [1]

                try:
                    values.append(float(value))
                    
                except Exception as e:
                    print('Non ho trovato il file.. {}' .format(e))

                my_list.append(element)

        return(my_list)

shampooFile = NumericalCSVFile('shampoo_parte2.txt')
shampoo = shampooFile.get_data()

print(shampoo)