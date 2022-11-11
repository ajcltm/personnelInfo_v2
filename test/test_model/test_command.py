import unittest
from personnelInfo.model import command, employee, appointment
from datetime import datetime

class TestCammand(unittest.TestCase):

    def setUp(self) -> None:
        self.raw_appionment = [
            {'name':'한창훈', 'id_':'200411001', 'ap_date':datetime(2004,12,1), 'ap_name':'입사(일반)', 'ap_department':'입사팀', 'ap_position':'차장', 'ap_level':'3급', 'ap_leader_position':None, 'description':None},
            {'name':'한창훈', 'id_':'200411001', 'ap_date':datetime(2005,12,1), 'ap_name':'부서이동', 'ap_department':'이동팀', 'ap_position':'차장', 'ap_level':'3급', 'ap_leader_position':None, 'description':None}
        ]

        self.raw_employee = {
            'id_':'200411001', 'name':'한창훈','birth':datetime(1973,12,14), 'sex':'남성', 'first_date':datetime(2004,12,1), 'last_date':None, 
            'department':'입사팀', 'department_date':datetime(2004,12,1), 'position':'차장', 
            'level':'3급', 'level_date':datetime(2004,12,1), 'leader_position':None, 'contract_state':'정규직'
            }


    def test_command(self):
        
        aset = appointment.AppointmentSet(data_set=self.raw_appionment)

        e = employee.Employee(**self.raw_employee)
        es = employee.EmployeeDataSet()
        es.dataSet[e.id_]=e

        # self.assertEqual(e.department, '입사팀')

        # e_ = command.MoveCommand().execute(employee=e, appointment=aset.data_set[1])
        # self.assertEqual(e_.department, '이동팀')

if __name__ == '__main__':
    unittest.main()