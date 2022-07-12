from personnelInfo.model import models

from typing import List
from pydantic import BaseModel, validator
from datetime import datetime


class Appointment(BaseModel):
    name:str
    id_:str
    ap_date:datetime
    ap_name:str
    ap_department:str
    ap_position:str
    ap_level:str
    ap_leader_position:str
    description:str

    @validator('*', always=True)
    def check_none_value(cls, v, values):
        if v == 'nan':
            return None
        return v

class AppointmentSet(BaseModel):
    data_set : List[Appointment]


class FAppointmentSet:

    def get_set(self):
        df = models.AppointmentModel().get_model().get_data()
        records = df.to_dict(orient='records')
        return AppointmentSet(data_set=records)
    



