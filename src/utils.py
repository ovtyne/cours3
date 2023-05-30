import json


def read_json_data():
    """
    Читает данный из файла operations.json
    :return: список транзакций
    """
    with open('operations.json', 'r', encoding='utf-8') as json_file:
        data = json.loads(json_file.read())
    return data


def filter_data(data):
    """
    Фильтрует список, оставляет только с датой и статусом перевода EXECUTED
    :param data: список транзакций
    :return: фильтрованный список
    """
    filtered_data = []
    for i in data:
        if 'date' not in i:
            continue
        if 'state' not in i:
            continue
        if i['state'] != "EXECUTED":
            continue
        filtered_data.append(i)
    return filtered_data


def sort_data(data):
    """
    Сортирует список в порядке убывания даты
    :param data: список транзакций
    :return: упорядоченный список
    """
    return sorted(data, key=lambda k: k['date'], reverse=True)


def transform_account(line):
    """
    Заменяет часть цифр в номере счета / карты символом *
    :param line: строка для сокрытия данных
    :return: обработанная строка
    """
    sublines = line.split(' ')
    number = sublines[-1]
    if sublines[0] == 'Счет':
        new_number = "**" + number[-4:]
    else:
        new_number = number[:4] + " " + number[4:6] + '** **** ' + number[-4:]
    line = " ".join(sublines[:-1]) + " " + new_number
    return line


def prepare_print_transaction(transaction):
    """
    Возвращает информацию о транзакции, подготовленную для печати
    :param transaction: тракзакция для вывода
    :return: страка для печати
    """
    t_description = ''
    t_from = ''
    t_to = ""

    date = transaction['date'][:10].split('-')
    t_date = date[2]+"."+date[1]+'.'+date[0]

    if 'description' in transaction:
        t_description = transaction['description']
    if 'from' in transaction:
        t_from = transform_account(transaction['from'])
    if 'to' in transaction:
        t_to = transform_account(transaction['to'])

    t_amount = transaction['operationAmount']['amount']
    t_name = transaction['operationAmount']['currency']['name']

    return f"{t_date} {t_description}\n{t_from} -> {t_to}\n{t_amount} {t_name}\n"


def print_last_transactions(data, number):
    """
    Выводит последние транзакции
    :param data: список транзакций
    :param number: кол-во элементов списка для вывода
    :return:
    """
    for i in range(number):
        print(prepare_print_transaction(data[i]))

