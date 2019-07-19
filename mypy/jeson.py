#do zrobienia

import json
if __name__ == '__main__':
    with open('','r',encoding='UTF-8')as f:
        lines = [line.replace('\n').split(';') for line in f]
    with open('iris.json','w', encoding='UTF-8')as f:
        f.write('[\n')
        for i in range(len(lines)):
            if i==len(lines):
                line_ending = '\n'
            else:
                line_ending = ',\n'
            f.write(f{json.dump(lines[i],line_ending)})

