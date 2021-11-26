class CSVFile():

    def __init__(self, name):
        self.name = name
        my_file = open(self.name, 'r')

        try:
            my_file = float(my_file)

        except Exception as e:
            printf('Non ho trovato il file {}' .format(e))

    def get_data(self):
        my_file = open(self.name, 'r')
        my_list = []
        my_file = float(my_file)

        try:
            my_file = float(my_file)
            
        for line in my_file:
            element = line.split(',')

            if element [0] != 'Date':
                my_list.append(element)
        return(my_list)

shampooFile = CSVFile('shampoo_sales_.txt')
shampoo = shampooFile.get_data()

print(shampoo)