import random
import time
import csv


if __name__ == '__main__':
    accounts = []
    with open('test.csv', mode='r', newline='', encoding='utf-8-sig') as File:
        reader = csv.reader(File)
        for row in reader:
            data = row[-1].split(';')
            address = data[0] + ' ' + data[1] + '-' + data[2]
            account = data[3]
            accounts.append({'address': address,
                             'account': account})
    accounts_winners = []
    while len(accounts_winners) < 33:
        winner = random.choice(accounts)
        print('Победитель-участник следующего этапа розыгрыша с номером лицевого счета №' + winner['account'] + 'по '
              'адресу: ' + winner['address'])
        accounts_winners.append(winner)
        accounts.remove(winner)
        time.sleep(5)
