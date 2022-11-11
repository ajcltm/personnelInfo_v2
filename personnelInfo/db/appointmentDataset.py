import sys
from pathlib import Path
sys.path.append(str(Path.cwd())) # 경로 추가
from personnelInfo.model import models
from personnelInfo.db import connect
from pydantic import BaseModel, validator
from Isql_v2 import sql
from datetime import datetime
import pandas as pd
from typing import Optional

class AppointmentModel(BaseModel):
    name : Optional[str]
    id_ : Optional[str]
    appointmentDate : Optional[datetime]
    appointmentName : Optional[str]
    department : Optional[str]
    workDepartment : Optional[str]
    position : Optional[str]
    level : Optional[str]
    leader : Optional[str]
    contractKind : Optional[str]
    appointmentDetail :Optional[str]
    reference :Optional[str]

    @validator('appointmentDate', pre=True)
    def timestamp_to_datetime(cls, v):
        if pd.isnull(v):
            return None
        return datetime.strptime(v.isoformat(), '%Y-%m-%dT%H:%M:%S')
    
    @validator('*')
    def nan_to_None(cls, v):
        if v == "nan":
            return None
        return v
        

class CreateTable:

    def __init__(self, con):
        self.db = con
        self.cur = self.db.cursor()

    def execute(self):
        sql_ = sql.CreateSql(model=AppointmentModel).get_create(
            name = 'text',
            id_ = 'text',
            appointmentDate = 'date',
            appointmentName = 'text',
            department = 'text',
            workDepartment = 'text',
            position = 'text',
            level = 'text',
            leader = 'text',
            contractKind = 'text',
            appointmentDetail = 'text',
            reference = 'text'
        )
        self.cur.execute(sql_)
        self.db.commit()

class DumpData:

    def __init__(self, con):
        self.db = con
        self.cur = self.db.cursor()

    def execute(self):
        df = models.AppointmentModel_v2().get_model().get_data()
        rawdataset = df.to_dict(orient='records')
        print(f'raw : \n {rawdataset[:2]}')
        dataset = [AppointmentModel(**data) for data in rawdataset]
        print(f'model : \n {dataset[:2]}')
        sql_ = sql.InsertSql(model=AppointmentModel).get_dump(dataset=dataset)
        self.cur.execute(sql_)
        self.db.commit()

if __name__ == '__main__':
    con = connect.Connector().get_connect()
    CreateTable(con).execute()
    DumpData(con).execute()