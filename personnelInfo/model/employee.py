from typing import Optional, Dict
from pydantic import BaseModel
from datetime import datetime

class Employee(BaseModel):
    id_:str
    name:str
    birth:datetime
    sex:str
    first_date:datetime
    last_date:Optional[datetime]=None
    department:str
    department_date:datetime
    position:str
    level:str
    level_date:datetime
    leader_position:Optional[str]=None
    contract_state:str

class EmployeeDataSet(BaseModel):

    dataSet : Dict = {}