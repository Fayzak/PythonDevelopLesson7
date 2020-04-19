from docxtpl import DocxTemplate
import datetime
from time import time


### Работа с docx ###


def get_context(name, series, count):  # Заполняем словарь значениями из файла и возвращаем его
    return {
        'brand': name,
        'model': series,
        'value': count,
    }


def from_template(name, series, count, template):  # Открываем документ, получаем и заполняем значения,
    tic = time()                                               # и сохраняем под новым именем
    template = DocxTemplate(template)
    context = get_context(name, series, count)
    template.render(context)
    template.save(name + '_' + str(datetime.datetime.now().date()) + '_data_set.docx')
    toc = time()
    return print("Время генерации отчёта 3: " + str(toc - tic))


def generate_report(name, series, count):
    template = 'data_set.docx'
    from_template(name, series, count, template)


with open('data') as f:  # Открываем файл и получаем значения
    for line in f:
        datalist = line.split(',')
brand = datalist[0]
model = datalist[1]
value = datalist[2]
generate_report(brand, model, value)

