import unittest
from pathlib import Path
import os
from personnelInfo.db import uniqueDataset, connect

class Test_1_uniqueDataset(unittest.TestCase):

    def setUp(self) -> None:
        self.path = Path.cwd().joinpath('test', 'test_db')
        
    def tearDown(self):
        os.remove(self.path.joinpath('personnelInfo.db'))

    def test_create_table(self):
        con = connect.Connector(folder_path=self.path).get_connect()
        uniqueDataset.CreateTable(con=con).execute()

class Test_2_dumpData(unittest.TestCase):

    def setUp(self) -> None:
        self.path = Path.cwd().joinpath('test', 'test_db')
        con = connect.Connector(folder_path=self.path).get_connect()
        uniqueDataset.CreateTable(con=con).execute()

    def test_dumpData(self):
        path = Path.cwd().joinpath('test', 'test_db')
        con = connect.Connector(folder_path=path).get_connect()
        uniqueDataset.DumpData(con=con).execute()

if __name__ == '__main__':
    unittest.main()