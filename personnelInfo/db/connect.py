from pathlib import Path
import sqlite3

class Connector:

    def __init__(self, folder_path='defualt'):
        if folder_path == 'defualt':
            self.path = Path().home().joinpath('Desktop', 'personnelInfo.db')
        else:
            self.path = folder_path.joinpath('personnelInfo.db')
        print(f'db path : {self.path}')
        
    def get_connect(self):
        con = sqlite3.connect(self.path)
        return con