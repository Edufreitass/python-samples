from datetime import date

from dateutil.relativedelta import relativedelta


def calcula_periodo_ferias(qtd_dias, data_inicial_desejada):
    data_inicial = date.fromisoformat(data_inicial_desejada)
    data_final = (data_inicial + relativedelta(days=qtd_dias)) - relativedelta(days=1)
    data_retorno = data_final + relativedelta(days=1)
    print(f'Período de férias: {fmt_dt(data_inicial)} até {fmt_dt(data_final)}')
    print(f'Seu retorno está previsto para o dia {fmt_dt(data_retorno)}')


def fmt_dt(data):
    return date.strftime(data, "%d/%m/%Y")


if __name__ == "__main__":
    qtd_dias = 14
    data_inicial_desejada = '2023-12-26'
    calcula_periodo_ferias(qtd_dias, data_inicial_desejada)
