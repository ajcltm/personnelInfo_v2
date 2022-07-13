from personnelInfo.utils import loader, processing
from typing_extensions import Protocol
from pydantic import BaseModel, validator
from datetime import datetime
import pandas as pd


class Command(Protocol):

    def execute(self):
        ...

class MoveCommand:

    def execute(self, employee, appointment):
        employee.department = appointment.ap_department
        return employee