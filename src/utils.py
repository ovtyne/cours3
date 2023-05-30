import json


def read_json_data():
    with open('operations.json', 'r', encoding='utf-8') as json_file:
        data = json.loads(json_file.read())
    return data


def filter_data(data):
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
    return sorted(data, key=lambda k: k['date'], reverse=True)


def transform_account(line):
    sublines = line.split(' ')
    number = sublines[-1]

    if sublines[0] == 'Счет':
        new_number = "**" + number[-4:]
    else:
        new_number = number[:4] + " " + number[4:6] + '** **** ' + number[-4:]
    line = " ".join(sublines[:-1]) + " " + new_number
    return line


def print_transaction(transaction):
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

    print(t_date + " " + t_description)
    print(f"{t_from} -> {t_to}")
    print(f"{t_amount} {t_name}")


def print_last_transactions(data, number):
    for i in range(number):
        print_transaction(data[i])
        print()