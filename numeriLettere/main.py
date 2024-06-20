def read_file(filename):

    words_to_digits = {
        'zero': 0,
        'uno': 1,
        'due': 2,
        'tre': 3,
        'quattro': 4,
        'cinque': 5,
        'sei': 6,
        'sette': 7,
        'otto': 8,
        'nove': 9
    }

    value = []

    with open(filename, 'r') as f:

        for line in f:

            #print(line)
            digits = []
            words = line.split()

            for word in words:

                if word == 'stop':
                    break

                if word in words_to_digits:
                    digits.append(words_to_digits[word])

            if digits:
                number = int(''.join(map(str, digits)))
                value.append(number)

    return value


def sum_numbers(numbers):

    sum = 0

    for number in numbers:

        sum += int(number)

    return sum


if __name__ == "__main__":

    #print list of numbers for each line
    #print(read_file('file.txt'))

    #print sum of numbers of total line
    print(sum_numbers(read_file('file.txt')))
