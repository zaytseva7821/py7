from genericpath import exists
import os
import controller
import view

def save_number():
    info = []
    last_name = input('Введите фамилию:\n')
    info.append(last_name)
    first_name = input('Введите имя:\n')
    info.append(first_name)
    phone_number = input('Введите номер телефона в формате +7**********:\n')
    info.append(phone_number)
    save_txt(info)
    save_csv(info)

def save_txt(info):
    file = 'phonebook.txt'
    with open(file, 'a', encoding='utf-8') as data:
        data.write(f'Фамилия: {info[0]}\nИмя: {info[1]}\nНомер телефона: {info[2]}\n\n')

def save_csv(info):
    file = 'phonebook.csv'
    with open(file, 'w', encoding='utf-8') as data:
        # data.write(f'Фамилия;Имя;Номер телефона;Описание\n')
        data.write(f'Фамилия: {info[0]}\nИмя: {info[1]}\nНомер телефона: {info[2]}\n\n')

def read_dict():
    file = 'phonebook.txt'
    if exists(file):
        with open(file, 'r', encoding='utf-8') as data:
            dictionary = data.read()
        print(dictionary)
    else:
        view.empty()

def create_html():
    file = 'phonebook.txt'
    if exists(file):
        data = open(file, encoding= "utf-8")
        text = data.readlines()
        data.close()
        style = 'style="font-size:22px;"'
        html = '<html>\n <head></head>\n <body>\n'
        for i in range(len(text)):
            html += "<p {}>{}</p>\n".format(style, text[i])
        html += '   </body>\n</html>'

        with open('phonebook.html', 'w') as page:
            page.write(html)
    
        return html
    else:
        view.empty()

def delete(text):
    file = f'phonebook.{text}'
    if exists(file):
        os.remove(file)
    else:
        print("Файл не найден")