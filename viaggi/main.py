class SearchCity():
    
    def __init__(self, name):

        self.name = name

    def get_data(self, dim):

        my_file = open(self.name, 'r')
        my_list = []
        i = 0
        flag = 0

        for line in my_file:

            element = line.split(',')

        #if element [0] != 'Stato':

        while i < dim and flag:
            
            if element [1] == 'Praga':
                flag = 1
                print(flag)
            break
            i = i + 1
            
        return flag

cityFile = SearchCity('viaggi.txt')
city = cityFile.get_data(55)

print(city)