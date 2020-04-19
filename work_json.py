import json
from time import time

with open('data2') as f:  # Открываем файл и получаем значения
    for line in f:
        datalist = line.split(',')

data_dict = [
    {'Brand': datalist[0], 'Model': datalist[1], 'Value': datalist[2]},
    {'Brand': datalist[3], 'Model': datalist[4], 'Value': datalist[5]},
    {'Brand': datalist[6], 'Model': datalist[7], 'Value': datalist[8]},
]

with open('data2.json', 'w', encoding="utf-8") as f:
    tic = time()
    for i in range(len(data_dict)):
        json.dump(data_dict[i], f)
    toc = time()
    time = toc - tic
    result = 'Время заполнения отчёта:' + str(time)
    f.write(result)