#Scrivete una funzione che sommi
#tutti gli elementi di una lista

from random import seed
from random import randint

#my_list = [16, 2, 7, 31, 5]
my_list = [randint(0, 100), randint(0, 50), randint(0, 150)]

def sum_list(my_list):
    sum = 0
    for i in range(len(my_list)):
        sum += my_list[i]
    return sum

print("Somma: {}" .format(sum_list(my_list)))