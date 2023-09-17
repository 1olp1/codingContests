lvl = 2


def main():
    inputs = []
    with open(f"lvl{lvl}_in", "r") as f:
        for line in f:
            inputs.append(line.split())

    for i, row in enumerate(inputs):
        print(f'Input {i}:')
        sales, payments = make_daily_sales_and_payments_list(row)

        invalid_days = []
        for j, sale in enumerate(sales):
            if not sale.sale == payments[j].payment:
                owed_money = sale.sale - payments[j].payment

                sales[j+1]
                invalid_days.append(str(sale.day))

        # Convert to correct output style
        invalid_days = ' '.join(invalid_days)
        print(invalid_days)


def make_daily_sales_and_payments_list(row):
    # Initialise lists of sales and payments
    sales = []
    payments = []

    # Loop through every item in inputs
    for i, element in enumerate(row):

        # Every third element contains the type of transaction
        if i % 3 == 0:
            day = int(row[i + 1])
            value = int(row[i + 2])
            if element == 'F':
                sale = DailySale(day, value)
                sales.append(sale)
            elif element == 'B':
                payments.append(DailyPayment(day, value))

    return sales, payments


class DailySale:
    def __init__(self, day, sale):
        self.day = day
        self.sale = sale


class DailyPayment:
    def __init__(self, day, payment):
        self.day = day
        self.payment = payment


if __name__ == "__main__":
    main()