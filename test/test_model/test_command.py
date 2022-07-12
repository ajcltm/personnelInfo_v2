import unittest
from personnelInfo.model import command, employee, appointment
from datetime import datetime

class TestCammand(unittest.TestCase):

    def test_command(self):
        raw_appionment_date = [
            {'name':'한창훈', 'id_':'200411001', 'ap_date':datetime(2004,12,1), 'ap_name':'입사(일반)', 'ap_department':'입사팀', 'ap_position':'차장', 'ap_level':'3급', 'ap_leader_position':None, 'description':None},
            {'name':'한창훈', 'id_':'200411001', 'ap_date':datetime(2005,12,1), 'ap_name':'부서이동', 'ap_department':'퇴직', 'ap_position':'차장', 'ap_level':'3급', 'ap_leader_position':None, 'description':None}
        ]
        
        command.MoveCommand()

if __name__ == '__main__':
    unittest.main()