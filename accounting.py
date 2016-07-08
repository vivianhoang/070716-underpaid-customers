def incorrect_pay(path):
    """Checking whether a customer paid the correct total for their melon.

    File is opened, split, and checked to see if customer paid the right \
    amount for melons by computating actual cost of melons and comparing \
    that to what the customer paid.
    """
    melon_cost = 1.00
    melon_file = open(path)  # opening the actual file and setting it to melon_file

    for line in melon_file:  # iterating through each line in the file
        line = line.rstrip()  # strips any whitespace at the end
        words = line.split('|')  # splits the line by 'pole' and returns string
        new_words = words[1:]  # customer number was unnecessary, so skipped

        name, quantity, actual_pay = new_words  # unpacking the list into variables
        quantity = int(quantity)  # converting list items into integers/floats
        actual_pay = float(actual_pay)

        actual_cost = melon_cost*quantity  # finding actual cost per customer

        if actual_cost > actual_pay:  # comparing actual cost and actual customer pay
            print name, "paid {:.2f}, actually expected {:.2f}".format(actual_pay, actual_cost)
            print name, "has underpaid for their melons."

        elif actual_cost < actual_pay:
            print name, "paid {:.2f}, actually expected {:.2f}".format(actual_pay, actual_cost)
            print name, "has overpaid for their melons."

        else:
            print "Every customer paid the correct total for their melons."

incorrect_pay('customer-orders.txt')  # calling function
