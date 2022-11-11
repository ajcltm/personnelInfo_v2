import sys
from pathlib import Path
sys.path.append(str(Path.cwd())) # 경로 추가
from personnelInfo.model import models
from personnelInfo.db import connect
from pydantic import BaseModel, validator
from Isql_v2 import sql
from datetime import datetime
from typing import Optional
import pandas as pd
import numpy as np

df = models.UniqueModel().get_model().get_data()

class UniqueModel(BaseModel):
    id_ : str
    name : str
    birth : datetime
    sex : str
    recruitmentDate : datetime
    resignationDate : Optional[datetime]

    @validator('birth', 'recruitmentDate', 'resignationDate', pre=True)
    def timestamp_to_datetime(cls, v):
        if pd.isnull(v):
            return None
        return datetime.strptime(v.isoformat(), '%Y-%m-%dT%H:%M:%S')
        



class CreateTable:

    def __init__(self, con):
        self.db = con
        self.cur = self.db.cursor()

    def execute(self):
        sql_ = sql.CreateSql(model=UniqueModel).get_create(
            id_ = 'text',
            name = 'text',
            birth = 'date',
            sex = 'text',
            recruitmentDate = 'date',
            resignationDate = 'date'
        )
        self.cur.execute(sql_)
        self.db.commit()

class DumpData:

    def __init__(self, con):
        self.db = con
        self.cur = self.db.cursor()

    def execute(self):
        df = models.UniqueModel().get_model().get_data()
        rawdataset = df.to_dict(orient='records')
        print(f'raw : \n {rawdataset[:2]}')
        dataset = [UniqueModel(**data) for data in rawdataset]
        print(f'model : \n {dataset[:2]}')
        sql_ = sql.InsertSql(model=UniqueModel).get_dump(dataset=dataset)
        self.cur.execute(sql_)
        self.db.commit()