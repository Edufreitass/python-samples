import csv


def csv_creator():
    try:
        print('Seja bem vindo ao Criador de CSV!')
        csv_path = input('Informe o path que o seu arquivo sera salvo (ex: C:\\Users\Eduardo\AppData\Local\Temp\\ficha_cadastral.csv): ')
        with open(csv_path, 'w', encoding='UTF8', newline='') as f:
            writer = csv.writer(f)
            header = input('Informe os cabeçalhos do seu arquivo (ex: nome,sobrenome,idade): ')
            # write the header
            writer.writerow(header.split(','))

            data = input('Informe os dados que serão inseridos (ex: eduardo,freitas,26): ')
            # write multiple rows
            writer.writerow(data.split(','))
    except Exception as e:
        print(f'Falha ao criar arquivo CSV: {e}')


def csv_cleaner():
    try:
        print('Seja bem vindo ao Limpador de Dados CSV!')
        csv_path = input('Informe o path do seu arquivo que sera limpado (ex: C:\\Users\Eduardo\AppData\Local\Temp\\ficha_cadastral.csv): ')
        with open(csv_path, 'r', encoding='UTF8') as f:
            reader = csv.reader(f)
            for row in reader:
                print(row)
    except Exception as e:
        print(f'Falha ao limpar arquivo CSV: {e}')


if __name__ == '__main__':
    csv_creator()
