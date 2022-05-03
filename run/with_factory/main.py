from factory.message_factory import RowsFactory

if __name__ == "__main__":
    users_file = "../../data/users.csv"
    cars_file = "../../data/cars.csv"

    users_file_pointer = open(users_file)
    cars_file_pointer = open(cars_file)

    factory = RowsFactory()

    for i in range(10):
        csv_line = users_file_pointer.readline()
        user_row = factory.create_row_instance("UserRow", csv_line)

        csv_line = cars_file_pointer.readline()
        car_row = factory.create_row_instance("CarRow", csv_line)

    print("Done")
