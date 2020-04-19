import csv
from time import time

fieldnames = ['Brand', 'Model', 'Value']
with open('data2') as f:  # Открываем файл и получаем значения
    for line in f:
        datalist = line.split(',')

data_dict = [
    {'Brand': datalist[0], 'Model': datalist[1], 'Value': datalist[2]},
    {'Brand': datalist[3], 'Model': datalist[4], 'Value': datalist[5]},
    {'Brand': datalist[6], 'Model': datalist[7], 'Value': datalist[8]},
]

with open('data2.csv', 'w', encoding="utf-8") as f:
    tic = time()
    writer = csv.DictWriter(f, delimiter=',', fieldnames=fieldnames)
    writer.writeheader()
    for i in range(len(data_dict)):
        writer.writerow(data_dict[i])
    toc = time()
    time = toc - tic
    result = 'Время заполнения отчёта:' + str(time)
    f.write(result)