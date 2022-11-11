from personnelInfo.db import connect
import os
from pathlib import Path

import unittest

class Test_connect(unittest.TestCase):

    def test_connect(self):
        connect.Connector()
        print(Path().cwd())
        print(os.listdir(Path().cwd()))


if __name__ == '__main__':
    unittest.main()