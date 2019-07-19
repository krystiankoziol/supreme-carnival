from statistics import mean

def main():
    with open('iris.data', 'r', encoding='UTF-8') as f:
        all_rows = []
        names = dict()
        for line in f:
            converted = __convert_line(line, names)
            all_rows.append(converted)
        #for i in range(0,4)
        #    print(calculate_stas([row[i] for row in all_rows]))


def __convert_line(line, names):
    line.replace("\n", "")
    splitted = line.split(',')
    for i in range(0, 4):
        splitted[i] = float(splitted[i])
    name = splitted[4]
    if name not in names:
        names[name] = len(names) + 1
    splitted[4] = name
    return tuple(splitted)

def print_string(string):
    print(string)


def print_hello_string():
    print('Hello World')
    print_string('Good Bye World')


def execute_function_n_times(function, n):
    for i in range(n):
        function()


if __name__ == "__main__":
    # execute_function_n_times(print_hello_string, 5)
    with open('iris.data', 'r', encoding='UTF-8') as f:
        all_list = []
        names = dict()
        for line in f:
            v1, v2, v3, v4, name = line.rstrip('\n').split(',')
            print((v1), (v2), (v3), (v4), name)
            if name not in names:
                names[name] = len(names) + 1
            row_data = (float(v1), float(v2), float(v3), float(v4), names[name])
            all_list.append(row_data)

    print(sum([flower[0] for flower in all_list]) / len(all_list))
    with open('iris.preproced', 'w', encoding='UTF-8') as f:
        for ith in range(0,4):
            f.write(str(ith)+ ';'.join( str(mean([flower[ith] for flower in all_list])))+'\n')


    print(all_list)
    print('koniec')
