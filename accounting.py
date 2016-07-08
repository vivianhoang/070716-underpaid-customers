def incorrect_pay(path):
    """Checking whether a customer paid the correct total for their melon.

    File is opened, split, and checked to see if customer paid the right \
    amount for melons by computating actual cost of melons and comparing \
    that to what the customer paid.
    """
    melon_cost = 1.00
    melon_file = open(path)

    for line in melon_file:
        line = line.rstrip()
        words = line.split('|')
        new_words = words[1:]

        name, quantity, actual_pay = new_words
        quantity = int(quantity)
        actual_pay = float(actual_pay)

        actual_cost = melon_cost*quantity

        if actual_cost != actual_pay:
            print name, "paid {:.2f}, actually expected {:.2f}".format(actual_pay, actual_cost)


incorrect_pay('customer-orders.txt')
