from os import read
import numpy as np


# Calcolare la media dei tempi di frenata (brake_rt) e di risposta allo stimolo (sec_rt)
# Contare il numero di mancate frenate (identificate dal valore “nan”

def read_file(filename):

    try:
        with open(filename, "r") as myfile:
            for line in myfile:
                #print(line.strip())
                element = line.split(',')
                if element[0] != 'on_exit':
                    lines = myfile.readline().strip().split(",")
                    print(lines)

    except FileNotFoundError:
        print("The file was not found.")

    except IOError:
        print("Error opening the file.")


def count_brake_rt(myfile):    #4
    count_brt = 0
    for line in myfile:
        if line[0] != 'nan':
            count_brt += 1

    print(count_brake_rt)
    return count_brt


def count_sec_rt(myfile):    #5
    count_srt = 0
    for line in myfile:
        if line[0] != 'nan':
            count_srt += 1

    print(count_sec_rt)
    return count_srt
    

if __name__ == "__main__":
    
    namefile = "drive.csv"
    
    read_file(namefile)
    
    count_brake_rt(namefile)
    count_sec_rt(namefile)
