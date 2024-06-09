def print_dir(filename):

    direction = {'N': 0, 'S': 0, 'E': 0, 'O': 0}

    with open(filename, 'r') as f:

        for line in f:
            #print(line.strip())
            dir, value = line.strip().split()
            value = int(value)
            direction[dir] += value

    #final_directions = []
    final_direction = ''
    final_value = 0

    net_nord = direction['N'] - direction['S']
    net_est = direction['E'] - direction['O']

    if net_nord != 0:
        final_direction += 'N' if net_nord > 0 else 'S'
        final_value += abs(net_nord)

    if net_est != 0:
        final_direction += 'E' if net_est > 0 else 'O'
        final_value += abs(net_est)

    if final_value == 0:
        print("Nessun spostamento")

    return final_direction, final_value


if __name__ == "__main__":
    file = 'esempio1.txt'
    print('file {}:'.format(file), print_dir(file))
