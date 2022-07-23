from collections import Counter


class TrackOrders:
    # aqui deve expor a quantidade de estoque
    def __init__(self):
        self.data = list()

    def __len__(self):
        return len(self.data)

    def add_new_order(self, customer, order, day):
        data_dict = dict()

        data_dict["customers"] = customer
        data_dict["orders"] = order
        data_dict["days"] = day
        self.data.append(data_dict)

    def get_most_ordered_dish_per_customer(self, customer):
        orders_per_customer = [
            row["orders"] for row in self.data if row["customers"] == customer
        ]

        return Counter(orders_per_customer).most_common(1)[0][0]

    def get_never_ordered_per_customer(self, customer):
        orders_per_customer = {
            row["orders"] for row in self.data if row["customers"] == customer
        }
        order = {row["orders"] for row in self.data}

        return order.difference(orders_per_customer)

    def get_days_never_visited_per_customer(self, customer):
        days = {row["days"] for row in self.data}
        visited_days = {
            row["days"] for row in self.data if row["customers"] in customer
        }

        return days.difference(visited_days)

    def get_busiest_day(self):
        days = [row["days"] for row in self.data if row["days"]]

        return Counter(days).most_common(1)[0][0]

    def get_least_busy_day(self):
        days = [row["days"] for row in self.data if row["days"]]

        return Counter(days).most_common()[-1][0]
