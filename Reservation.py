print("\n * MAIN MENU *\n\n 1-) Booking \n 2-) Print the hall")
print(" 3-) New event \n 4-) Total endorsement \n 0-) Quit \n ")

# ---- Creating a hall ---- #
income = 0
hall = []
available_seats = [100, 100, 100, 100]
for i in range(20):
    line = []
    for j in range(20):
        x = "-"
        line.append(x)
    hall.append(line)


# ---- Booking Functions ---- #

def asking_ticket_amount():
    while True:
        try:
            ticket_amount = int(input("How many ticket do you want to buy? (1 - 20) : "))
            if ticket_amount <= 0 or ticket_amount > 20:
                raise ValueError
            break
        except ValueError:
            print("It is not a proper enter.")
    return ticket_amount


def type_one_booking():
    start_number = 0
    end_number = 0
    price = 0
    ticket_amount = asking_ticket_amount()
    sold = 0
    if category_number == "1":
        start_number = 0
        end_number = 10
    elif category_number == "3":
        start_number = 10
        end_number = 20
    if ticket_amount <= available_seats[int(category_number) - 1]:
        for i in range(start_number, end_number):
            for j in range(5, 15):
                if sold < ticket_amount and hall[i][j] != "X":
                    hall[i][j] = "X"
                    sold = sold + 1
                    available_seats[int(category_number) - 1] = available_seats[int(category_number) - 1] - 1
                    print(str(i + 1), "-", str(j + 1))
        price = price + calculate_price(category_number, ticket_amount)
        print("Price :", price)
    else:
        print("Not enough space")


def type_two_booking():
    start_number = 0
    end_number = 0
    price = 0
    ticket_amount = asking_ticket_amount()
    sold = 0
    if category_number == "2":
        start_number = 0
        end_number = 10
    elif category_number == "4":
        start_number = 10
        end_number = 20
    if ticket_amount <= available_seats[int(category_number) - 1]:
        for i in range(start_number, end_number):
            for j in range(0, 20):
                if j < 5 and sold < ticket_amount and hall[i][4 - j] != "X":
                    hall[i][4 - j] = "X"
                    sold = sold + 1
                    available_seats[int(category_number) - 1] = available_seats[int(category_number) - 1] - 1
                    print(str(i + 1), "-", str((4 - j) + 1))

                if j > 14 and sold < ticket_amount and hall[i][j] != "X":
                    hall[i][j] = "X"
                    sold = sold + 1
                    available_seats[int(category_number) - 1] = available_seats[int(category_number) - 1] - 1
                    print(str(i + 1), "-", str(j + 1))
        price = price + calculate_price(category_number, ticket_amount)
        print("Price :", price)
    else:
        print("Not enough space")


# ---- Reading File for Endorsement ---- #
file = open("discount.txt", "r")
lines = file.readlines()
lines_array = []
lines_two_dimensional = []

for i in range(len(lines)):
    lines_array.append(lines[i][0:-1])    # I get rid of the \n
    element = lines_array[i].split("-")
    lines_two_dimensional.append(element)

file.close()


def calculate_price(category_num, ticket_amount):
    global income
    price_per_ticket = 1
    discount_rate = 0
    for i in range(1, 5):
        if category_num == lines_two_dimensional[i][0]:
            price_per_ticket = lines_two_dimensional[i][1]
    for i in range(5, len(lines_array)):
        if lines_two_dimensional[i][2] == "M":
            lines_two_dimensional[i][2] = lines_two_dimensional[0][1]
        if category_num == lines_two_dimensional[i][0]:
            if int(lines_two_dimensional[i][1]) <= ticket_amount <= int(lines_two_dimensional[i][2]):
                discount_rate = lines_two_dimensional[i][3]
    income = income + int(price_per_ticket) * int(ticket_amount) * (100 - int(discount_rate)) / 100
    return int(price_per_ticket) * int(ticket_amount) * (100 - int(discount_rate)) / 100


# ---- Main ---- #
while True:
    operation = False
    while not operation:
        operation_number = input("Enter the number of operation you want: ")

        # ---- Booking ---- #
        if operation_number == "1":
            category = False
            while not category:
                category_number = input("Which category do you prefer? :")
                if category_number == "1" or category_number == "3":
                    type_one_booking()
                    category = True
                elif category_number == "2" or category_number == "4":
                    type_two_booking()
                    category = True
                else:
                    print("It is not a proper enter. ")
            operation = True

        # ---- Print the hall ---- #
        elif operation_number == "2":
            for i in range(20):
                print(*hall[i])
            operation = True

        # ---- New Event ---- #
        elif operation_number == "3":
            for i in range(20):
                for j in range(20):
                    hall[i][j] = "-"
            operation = True

        # ---- Total endorsement ---- #
        elif operation_number == "4":
            print("Total income =", income)
            operation = True

        # ---- Quit ---- #
        elif operation_number == "0":
            print("Goodbye! :)")
            exit()

        else:
            print("It is not a proper enter")
