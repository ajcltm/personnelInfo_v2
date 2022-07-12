import unittest
from personnelInfo.model import models

class TestUniqueModel(unittest.TestCase):

    def test_print_model(self):
        df = models.UniqueModel().get_model().get_data()
        print(df.head())

class TestAppointmentModel(unittest.TestCase):

    def test_print_model(self):
        df = models.AppointmentModel().get_model().get_data()
        print(df.head())

if __name__ == '__main__':
    unittest.main()