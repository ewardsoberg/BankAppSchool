import json
name = 'Bosse Bildoktorn'
insert_dict = {}
number_list = []
with open('db_files/bank.json', 'r') as file:
    data = json.load(file)
    for data in data['customers']:
        for accounts in data['accounts']:
            if accounts:
                number_list.append(accounts['account_number'])

with open('db_files/bank.json', 'r+') as f:
    data = json.load(f)
    for data in data['customers']:
        if data['name'] == name:
            insert_dict['account_number'] = (number_list[-1]+1)
            insert_dict['currency'] = 'SEK'
            insert_dict['amount'] = 23
            print(insert_dict)
            data['accounts'].append(insert_dict)
            file.seek(0)
            json.dump(data, file)
