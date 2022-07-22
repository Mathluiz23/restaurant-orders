import csv


def get_most_orders_by_maria(orders):
    maria_orders = dict()

    for name, order, _day in orders:

        if name == "maria":
            if order not in maria_orders:
                maria_orders[order] = 1
            else:
                maria_orders[order] += 1

    return max(maria_orders, key=maria_orders.get)


def get_quantity_arnaldo_hamburguers(orders):
    arnaldo_hamburgers = 0

    for name, order, _day in orders:

        if name == "arnaldo" and order == "hamburguer":
            arnaldo_hamburgers += 1

    return arnaldo_hamburgers


def get_orders_and_days_joao(orders):
    joao_orders = set()
    joao_days = set()
    all_days = set()
    full_orders = set()

    for name, order, day in orders:

        all_days.add(day)
        full_orders.add(order)

        if name == "joao":
            joao_orders.add(order)
            joao_days.add(day)

    return [
        full_orders.difference(joao_orders),
        all_days.difference(joao_days),
    ]


def analyze_log(path_to_file):
    if not path_to_file.endswith(".csv"):
        raise FileNotFoundError(f"Extensão inválida: '{path_to_file}'")

    try:
        with open(path_to_file) as file:
            file_reader = list(csv.reader(file, delimiter=",", quotechar='"'))

            maria_orders = get_most_orders_by_maria(file_reader)
            arnaldo_hamburguers = get_quantity_arnaldo_hamburguers(file_reader)
            joao_orders = get_orders_and_days_joao(file_reader)[0]
            joao_days = get_orders_and_days_joao(file_reader)[1]

            new_file = open("data/mkt_campaign.txt", "w")

            new_file.write(
                f"{maria_orders}\n"
                f"{arnaldo_hamburguers}\n"
                f"{joao_orders}\n"
                f"{joao_days}\n"
            )

    except FileNotFoundError:
        raise FileNotFoundError(f"Arquivo inexistente: '{path_to_file}'")
