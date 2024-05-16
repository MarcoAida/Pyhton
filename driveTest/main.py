import numpy as np

# Calcolare la media dei tempi di frenata (brake_rt) e di risposta allo stimolo (sec_rt)
# Contare il numero di mancate frenate, identificate dal valore “nan”


def read_file(filename):

    data = []

    try:
        with open(filename, "r") as myfile:
            for line in myfile:
                #print(line.strip())
                element = line.strip()
                if element and not element.endswith('on_exit'):    #skip first line
                    #print(element)
                    data.append(element.split(','))
        return data

    except FileNotFoundError:
        print("The file was not found.")

    except IOError:
        print("Error opening the file.")

    return data


def process_data(data):
    brake_times = []  #4
    response_times = []  #5
    missed_brakes = 0
    missed_response = 0

    for entry in data:
        brake_time = entry[3]
        response_time = entry[4]

        if brake_time.lower() == 'nan':
            missed_brakes += 1
        else:
            brake_times.append(float(brake_time))    #(brake_rt)

        if response_time.lower() == 'nan':
            missed_response += 1
        else:
            response_times.append(float(response_time))    #(sec_rt)

    #print(brake_times)
    #print(response_times)

    average_brake = np.mean(brake_times)
    averaga_response = np.mean(response_times)

    return average_brake, averaga_response, missed_brakes, missed_response


if __name__ == "__main__":

    namefile = "drive.csv"

    data = read_file(namefile)

    #print(data)

    if data:
        average_brake_time, average_response_time, missed_brakes, missed_response = process_data(
            data)
        print("Average Brake Time: {}".format(average_brake_time))
        print("Average Response Time: {}".format(average_response_time))
        print("Total Missed Brakes: {}".format(missed_brakes))
        print("Total Missed Response: {}".format(missed_response))
    else:
        print("No data to process.")
