from pydantic import BaseModel
from datetime import datetime

class Employee(BaseModel):
    id_:str
    name:str
    birth:datetime
    sex:str
    first_date:datetime
    last_date:datetime
    department:str
    department_date:str
    position:str
    level:str
    level_date:str
    leader_position:str
    contract_state:str
