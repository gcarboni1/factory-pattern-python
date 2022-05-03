from unittest import TestCase

from factory.message_factory import RowsFactory
from messages import UserRow, CarRow


class FactoryTestSuite(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.factory = RowsFactory()

    def test_factory_loader_with_user(self):
        csv_line = "1,Edgardo,Van der Krui,evanderkrui0@bloglines.com"
        user_row = self.factory.create_row_instance("UserRow", csv_line)
        self.assertIsInstance(user_row, UserRow)

        self.assertEqual(user_row.user_id, "1")
        self.assertEqual(user_row.first_name, "Edgardo")
        self.assertEqual(user_row.last_name, "Van der Krui")
        self.assertEqual(user_row.email, "evanderkrui0@bloglines.com")

    def test_factory_loader_with_car(self):
        csv_line = "1,X6,WAU4FAFL9AA304654,BMW"
        car_row = self.factory.create_row_instance("CarRow", csv_line)
        self.assertIsInstance(car_row, CarRow)

        self.assertEqual(car_row.car_id, "1")
        self.assertEqual(car_row.model, "X6")
        self.assertEqual(car_row.vin, "WAU4FAFL9AA304654")
        self.assertEqual(car_row.builder, "BMW")

    def test_factory_loader_raise_exception(self):
        with self.assertRaises(Exception):
            self.factory.create_row_instance("WRONG_CLASS", "")
