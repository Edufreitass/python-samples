import random
import csv
from faker import Faker
from datetime import datetime


# Instalação do Faker:
# Para utilizar este código, é necessário instalar a biblioteca Faker.
# Você pode instalar o Faker utilizando o pip. Execute o seguinte comando no terminal:
# pip install Faker


fake = Faker("pt_BR")


# Gerador de dados fictícios para um dataset de vendas.


# Solicitar informações do usuário
num_records = int(input("Digite a quantidade de registros a serem gerados: "))  # Número de registros a serem gerados
mes = int(input("Digite o número do mês desejado: "))  # Mês dos registros
ano = int(input("Digite o ano desejado: "))  # Ano dos registros
num_cpf = int(input("Digite a quantidade de clientes: "))  # Quantidade de clientes
num_op = int(input("Digite a quantidade de operadoras: "))  # Quantidade de operadoras
mes_ano = f"{mes:02d}-{ano:04d}"  # Data no formato MM-AAAA


# Dados para o dataset
start_hour = 8  # Hora inicial das vendas
end_hour = 22  # Hora final das vendas
product_dict = {
  # Dicionário contendo produtos e seus preços
  "Arroz": 21.70,
  "Feijão": 15.50,
  "Açúcar": 25.50,
  # ... (Adicione outros produtos aqui)
}
operators = [fake.first_name_female() for _ in range(num_op)]  # Nomes de operadoras fictícias
operations = ["pix", "cartão_credito", "cartão_debito", "dinheiro"]  # Tipos de operações


# Variáveis de controle
min_cpf_percentage = 0.05  # Porcentagem mínima de CPFs únicos
max_cpf_percentage = 0.3  # Porcentagem máxima de CPFs únicos


# Calcula a quantidade de CPFs com base nas porcentagens definidas
min_cpf = int(num_cpf * min_cpf_percentage)
max_cpf = int(num_cpf * max_cpf_percentage)
num_cpfs = random.randint(min_cpf, max_cpf)


# Gera CPFs aleatórios
all_cpfs = [fake.cpf() for _ in range(num_cpfs)]


# Gera os registros do dataset
dataset = []
for _ in range(num_records):
  cpf = random.choice(all_cpfs)
  hora = f"{random.randint(start_hour, end_hour):02d}:{random.randint(0, 59):02d}"  # Formatação da hora
  dia = random.randint(1, 30)  # Dia da venda
  data = datetime(year=ano, month=mes, day=dia).strftime("%d/%m/%Y")  # Data da venda formatada
  produto = random.choice(list(product_dict.keys()))  # Escolhe um produto aleatoriamente
  preço = product_dict[produto]  # Preço do produto escolhido
  quantidade = random.randint(1, 10)  # Quantidade do produto vendida
  pdv = random.randint(1, 21)  # Ponto de venda
  operadora = random.choice(operators)  # Operadora escolhida aleatoriamente
  operação = random.choice(operations)  # Tipo de operação escolhido aleatoriamente
  total = round(preço * quantidade, 2)  # Cálculo do total da venda
  dataset.append([cpf, hora, data, produto, preço, quantidade, pdv, operadora, operação, total])


# Escreve os registros no arquivo CSV
filename = f"venda_{mes_ano}.csv"
with open(filename, "w", newline="") as csvfile:
  csvwriter = csv.writer(csvfile)
  csvwriter.writerow(["cpf", "hora", "data", "produto", "preço", "quantidade", "pdv", "operadora", "operação", "total"])
  csvwriter.writerows(dataset)


print(f"Dataset gerado e salvo como {filename}")  # Indica o nome do arquivo gerado
