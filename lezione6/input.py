class CSVFile():

    def __init__(self, name):
        self.name = name
        my_file = isinstance(name, CSVFile)

        #if(my_file is None):
            #raise Exception('Ho avuto un errore, ecco il parametro che lo ha generato {}'.format(name))

        try:
            my_file = open('shampoo_sal.txt', 'r')

        except Exception as e:
            print('Non ho trovato il file.. {}' .format(e))

    def get_data(self, start = None, end = None):
        my_file = open(self.name, 'r')
        my_list = []
        
        try:
            my_file = open('shampoo_sal.txt', 'r')

        except Exception as e:
            print('Non ho trovato il file.. {}' .format(e))
        
        if(start == 0):
            raise Exception('Ho avuto un errore, ecco il parametro che lo ha generato {}'.format(start))

        if(end is None):
            raise Exception('Ho avuto un errore, ecco il parametro che lo ha generato {}'.format(end))

        for line in my_file:
            element = line.split(',')
            element[1] = element[1].strip()

            if element [0] != 'Date':
                my_list.append(element)

        return(my_list)

shampooFile = CSVFile('shampoo_sales_.txt')
shampoo = shampooFile.get_data(0, 11)

print(shampoo)