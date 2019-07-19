import json
from functools import reduce

if __name__ == '__main__':
    with open('iris.json','r',encoding='UTF-8') as f:
        result = json.load(f)
    result =list(map(lambda row:[float(el) for el in row], result))
    print (result)

    result=list(filter(lambda row: row[4] == 2, result))
    print (result)

    #mapaowanie z LC
    result = [[str(element) for element in row] for row in result]
    print (result)

    #filtrowanie z LC
    result = [row for row in result if float(row[1]) > 2]
    print (result)

    #Reduce
    numbers [1,2,3,4]

    re = reduce(lambda l, r:l*r, numbers)
    print(re)
