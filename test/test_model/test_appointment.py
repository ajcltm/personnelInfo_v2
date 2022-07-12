import unittest
from personnelInfo.model import appointment

class TestAppointmentSet(unittest.TestCase):

    def test_appointment_set(self):
        ap_set = appointment.FAppointmentSet().get_set()
        print(ap_set.data_set[:2])

if __name__ == '__main__':
    unittest.main()