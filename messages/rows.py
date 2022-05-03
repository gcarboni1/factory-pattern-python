from abc import ABC, abstractmethod


class CsvRow(ABC):
    """Abstract Class"""

    @abstractmethod
    def print(self):
        pass


class UserRow(CsvRow):
    user_id = None
    first_name = None
    last_name = None
    email = None

    def __init__(self, csv_line: str):
        columns_array = csv_line.split(",")
        user_id = columns_array[0]
        first_name = columns_array[1]
        last_name = columns_array[2]
        email = columns_array[3]

        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email

    def print(self):
        print(f"{self.user_id},"
              f"{self.first_name},"
              f"{self.last_name},"
              f"{self.email}",
              end="")


class CarRow(CsvRow):
    car_id = None
    model = None
    vin = None
    builder = None

    def __init__(self, csv_line: str):
        line_splitted = csv_line.split(",")
        car_id = line_splitted[0]
        model = line_splitted[1]
        vin = line_splitted[2]
        builder = line_splitted[3]

        self.car_id = car_id
        self.model = model
        self.vin = vin
        self.builder = builder

    def print(self):
        print(f"{self.car_id},"
              f"{self.model},"
              f"{self.vin},"
              f"{self.builder}"
              , end="")
