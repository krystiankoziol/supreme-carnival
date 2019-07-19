import pickle
from statistics import mean


def serialize_pickle (pickle_file, iris):
    with open(pickle_file,'wb') as f:
         pickle.dump(iris,f)

def deserialize_pickle (pickle_file):
    with open(pickle_file,'rb') as f:
        iris = pickle.load(f)
    return iris


def serialize_json (json_file, iris):
    describe= ['a','b','c','d']
    result = '[\n[\n'
    for elements in iris:
        result += '{'
        for element in elements:
            result += str(element) + ','
        result += '}'
    result += ']\n]\n'

    return result
    # with open(json_file,'w') as f:
    #      json.dump(employees,f)

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
    serialize_pickle('iris.pickle', all_rows)
    print(serialize_json('json_file', all_rows))

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
    # else:
    #     print(f'')
