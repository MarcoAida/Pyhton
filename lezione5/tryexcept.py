class CSVFile():

    def __init__(self, name):
        self.name = name
        my_file = open(self.name, 'r')

        try:
            my_file = float(self.name)

        except Exception as e:
            print('Non ho trovato il file.. {}' .format(e))

    def get_data(self):
        my_file = open(self.name, 'r')
        my_list = []

        try:
            my_list = float(my_file)

        except Exception as e:
            print('Non ho trovato il file.. {}' .format(e))

        for line in my_file:
            element = line.split(',')
            element[1] = element[1].strip()

            if element [0] != 'Date':
                my_list.append(element)

        return(my_list)

shampooFile = CSVFile('shampoo_sales_.txt')
shampoo = shampooFile.get_data()

print(shampoo)