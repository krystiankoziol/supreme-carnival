from statistics import mean


def main():
    with open('iris.data', 'r', encoding='utf-8') as f:
        all_rows = []
        names = dict()
        for line in f:
            converted = __convert_line(line, names)
            all_rows.append(converted)
        stats = {}
        for i in range(0, 4):
            ith_column = [row[i] for row in all_rows]
            stats[i] = calculate_stats(ith_column)
    with open('iris_preprocessed2.data', 'w', encoding='utf-8') as f:
        for row in all_rows:
            f.write(';'.join([str(e) for e in row]) + '\n')
    with open('iris.stats', 'w', encoding='utf-8') as f:
        for key in stats:
            f.write(str(stats[key]) + '\n')


def __convert_line(line, names):
    line.replace("\n", "")
    splitted = line.split(",")
    for i in range(0, 4):
        splitted[i] = float(splitted[i])
    name = splitted[4]
    if name not in names:
        names[name] = len(names) + 1
    splitted[4] = names[name]
    return tuple(splitted)


def calculate_stats(column):
    smallest = min(column)
    largest = max(column)
    average = mean(column)
    return {"min": smallest, "max": largest, "average": average}


if __name__ == '__main__':
    try:
        main()
    except (FileNotFoundError, FileExistsError, EOFError) as e:
        print(f'Something failed with {e.__class__.__name__}')
    except Exception as e:
        print(f'Something failed with {e.__class__.__name__}')
    else:
        print(f'')
