# a) Estrarre e contare le biblioteche di un comune (chiesto come input all’utente) sulla base dei dati contenuti nel file biblioteche.csv.

# b) Creare delle funzioni di utilità per accedere ad un file e per terminare l’accesso ad un file (“apertura e chiusura”): queste funzioni devono intercettare eventuali errori e terminare il programma con un messaggio appropriato.

# c) Utilizzare una tupla “biblioteca” che rappresenti una riga del file biblioteche.csv. Possibilmente fare una funzione che legga una riga e ritorni la tupla relativa.


def leggi_file(myfile):

    try:
        myfile = open("biblioteche.csv", "r")
        return myfile.readlines()

    except FileNotFoundError:
        print("File non trovato")
        exit(1)

    except Exception as e:
        print("I/O error", e)
        exit(1)


def close_file(file_handle):

    try:
        file_handle.close()
        print("Il file è stato chiuso correttamente.")

    except Exception as e:
        print("Errore durante la chiusura del file:", e)
        exit(1)


def extract_line(comune, lines):

    mylist = []
    count = 0

    for line in lines:

        line = line.rstrip()
        element = line.split(';')

        if len(element) >= 3 and element[2].lower() == comune:

            mylist.append(element)
            count += 1

    #print(count)
    return mylist, count


def read_tuplaline(elements):

    try:
        biblioteca = tuple(elements)
        return biblioteca

    except Exception as e:
        print("Errore durante la creazione della tupla:", e)
        return None


if __name__ == "__main__":

    myfile = "biblioteche.csv"

    lines = leggi_file(myfile)

    print("Digita un comune: ")
    comune = input().lower()

    mylistB, count = extract_line(comune, lines)

    if mylistB:
        for biblioteche in mylistB:
            print(biblioteche)

        print("\nNumero di biblioteche a {}: {}".format(
            comune.capitalize(), count))

    else:
        print("There are not bibli in {}.".format(comune.capitalize()))
        exit(1)
        #close_file(myfile)

    try:
        print("\nDigita un riga da leggere: ")
        readline = int(input())

        if readline >= 1 and readline <= count:
            line = mylistB[readline - 1]
            biblioteca = read_tuplaline(line)

            if biblioteca:
                print("Riga {}: {}".format(readline, biblioteca))
            else:
                print("Errore nella lettura della riga.")

        else:
            print("La linea {} non è presente nel file.".format(readline))

    except ValueError:
        print("Input non valido. Inserire un numero intero.")

    close_file(myfile)
