def read_file(filename):

    expressions = []

    with open('dati.txt', 'r') as f:

        for line in f:

            line = line.strip()

            if not line:
                continue

            if line.endswith(';'):
                line = line[:-1]  #non considero l'ultimo carattere

            left_part, rigth_part = line.split('=')

            left_number = left_part.split('+')
            right_number = rigth_part.split('+')

            left_sum = sum(int(num) for num in left_number)
            right_sum = sum(int(num) for num in right_number)

            expressions.append((left_sum, right_sum, line))

    return expressions


def check_expression(expressions):

    result = []

    for left_sum, right_sum, line in expressions:

        if left_sum == right_sum:
            result.append("Correct: {} = {}".format(left_sum, right_sum))
        else:
            result.append("Inorrect: {} != {}".format(left_sum, right_sum))

    return result


if __name__ == "__main__":

    #print(check_expression(read_file('dati.txt')))

    file = 'dati.txt'

    expressions = read_file(file)

    results = check_expression(expressions)

    for result in results:
        print(result)
