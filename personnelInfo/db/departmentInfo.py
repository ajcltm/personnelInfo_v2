import sys
from pathlib import Path
sys.path.append(str(Path.cwd())) # 경로 추가
from personnelInfo.model import models
from personnelInfo.db import connect
from pydantic import BaseModel, validator
from Isql_v2 import sql
from datetime import datetime, date
import pandas as pd
from typing import Optional

class DepartmentInfo(BaseModel):
    start : Optional[date]
    end : Optional[date]
    devision : Optional[str]
    department : Optional[str]
    department_order : int


    @validator('start', 'end', pre=True)
    def timestamp_to_datetime(cls, v):
        if pd.isnull(v):
            return None
        return datetime.strptime(v.isoformat(), '%Y-%m-%dT%H:%M:%S')
        

class CreateTable:

    def __init__(self, con):
        self.db = con
        self.cur = self.db.cursor()

    def execute(self):
        sql_ = sql.CreateSql(model=DepartmentInfo).get_create(
            start = 'date',
            end = 'date',
            devision = 'text',
            department = 'text',
            department_order = 'integer',
        )
        self.cur.execute(sql_)
        self.db.commit()

class DumpData:

    def __init__(self, con):
        self.db = con
        self.cur = self.db.cursor()

    def execute(self):
        df = models.DepartmentInfo().get_model().get_data()
        rawdataset = df.to_dict(orient='records')
        print(f'raw : \n {rawdataset[:2]}')
        dataset = [DepartmentInfo(**data) for data in rawdataset]
        print(f'model : \n {dataset[:2]}')
        sql_ = sql.InsertSql(model=DepartmentInfo).get_dump(dataset=dataset)
        self.cur.execute(sql_)
        self.db.commit()

if __name__ == '__main__':
    con = connect.Connector().get_connect()
    CreateTable(con).execute()
    DumpData(con).execute()