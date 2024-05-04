#Sia dato un file che contiene una matrice rettangolare di interi positivi preceduta dalle sue dimensioni (separate dal carattere “X”)

#Come esempio si consideri il file “in.txt” con il seguente contenuto (5X6)

#Scrivere uno script python che prenda il nome di un file e produca un file “out.txt” eliminando le righe che hanno come primo valore 0 ed invertendo l’ordine delle righe.

#Il numero di righe (nella prima riga, quella delle dimensioni) deve essere riscritto in modo che corrisponda alle righe della nuova matrice.

#Nell’esempio di cui sopra il contenuto del file al termine dell’esecuzione deve essere il seguente (3X6):

#2 3 3 3 0 1
#3 2 5 2 0 0
#1 3 4 8 9 5

myfile = open("in.txt", "r")

lines = myfile.readline().strip().split("X")

len_row = int(lines[0])

len_col = int(lines[1])

filter_lines = []

for line in myfile:
    if line[0] != "0":
        filter_lines.append(line)

filter_lines.reverse()

len_fil_row = 0

for line in filter_lines:
    len_fil_row += 1

myfile.flush()

myfile.close()

if __name__ == "__main__":

    for line in filter_lines:
        print(line, end="")

    with open("out.txt", "w") as outfile:
        outfile.write(str(len_fil_row) + "X" + str(len_col) + "\n")
        for line in filter_lines:
            outfile.write(line)
