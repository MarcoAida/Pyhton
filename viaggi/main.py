class SearchCity:

    def __init__(self, filename):

        self.filename = filename

    def get_data(self, city_name):

        with open(self.filename, 'r') as file:

            for line in file:
                elements = line.strip().split(',')

                if len(elements) > 1 and elements[1] == city_name:
                    return True

        return False


if __name__ == "__main__":

    city_search = SearchCity('viaggi.txt')

    #insert name of city to find
    print('City to find: ')
    city_input = input().lower

    city_found = city_search.get_data(city_input().capitalize())

    print(city_found)
