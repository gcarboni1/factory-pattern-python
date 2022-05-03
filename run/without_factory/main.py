from messages.rows import UserRow, CarRow


def create_row_instance(message_type, csv_line):
    if message_type == "UserRow":
        return UserRow(csv_line)
    elif message_type == "CarRow":
        return CarRow(csv_line)


if __name__ == "__main__":
    users_file = "../../data/users.csv"
    cars_file = "../../data/cars.csv"

    users_file_pointer = open(users_file)
    cars_file_pointer = open(cars_file)

    num_rows_to_read = 10

    for i in range(num_rows_to_read):
        csv_line = users_file_pointer.readline()
        if csv_line != "":
            user_row = create_row_instance("UserRow", csv_line)
            assert isinstance(user_row, UserRow)
            user_row.print()

    print("\n--")
    for y in range(num_rows_to_read):
        csv_line = cars_file_pointer.readline()
        if csv_line != "":
            car_row = create_row_instance("CarRow", csv_line)
            assert isinstance(car_row, CarRow)
            car_row.print()
