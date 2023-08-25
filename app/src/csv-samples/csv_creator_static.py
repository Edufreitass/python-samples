import csv

from faker import Faker

fake = Faker()


def csv_creator():
    try:
        csv_path = 'C:\\Users\Eduardo\AppData\Local\Temp\\ficha_cadastral.csv'
        with open(csv_path, 'w', encoding='UTF8', newline='') as f:
            writer = csv.writer(f)
            header = 'nome'
            # write the header
            writer.writerow(header.split(','))

            data = fake.first_name()
            # write multiple rows
            writer.writerow(data.split(','))
    except Exception as e:
        print(f'Falha ao criar arquivo CSV: {e}')


if __name__ == '__main__':
    csv_creator()
