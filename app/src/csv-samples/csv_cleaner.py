import csv


def csv_cleaner():
    try:
        print('Seja bem vindo ao Limpador de Dados CSV!')
        csv_path = input('Informe o path do seu arquivo que sera limpado (ex: C:\\Users\Eduardo\AppData\Local\Temp\\ficha_cadastral.csv): ')
        with open(csv_path, 'r+') as f:
            reader = csv.reader(f)
            for row in reader:
                row.clear()
    except Exception as e:
        print(f'Falha ao limpar arquivo CSV: {e}')


if __name__ == '__main__':
    csv_cleaner()
