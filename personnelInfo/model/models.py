from personnelInfo.model import command
from personnelInfo.utils import loader, processing
from personnelInfo.config import config
import pandas as pd


class SloadNProcessingModel:

    def __init__(self, ILoader:loader.ILoader, IProcessing:processing.IProcessing)->None:
        self.loader = ILoader
        self.processing = IProcessing

    def get_data(self)->pd.DataFrame:
        _df = self.loader.load()
        _df = self.processing.processing(_df)
        return _df


class UniqueModel:

    def get_model(self):
        return SloadNProcessingModel(ILoader=self.get_loader(), IProcessing=self.get_processing())
    
    def get_loader(self):
        file_path = config.main_path.joinpath('0. 직원고유정보.csv')
        return loader.Loader(file_path=file_path)

    def get_processing(self):
        prc = processing.Composit()
        p1 = processing.Rename(cols=['id_', 'name', 'birth', 'sex', 'veryFirstPostionLevel', 'recruitmentDate', 'resignationDate'])
        p2 = processing.ApplyDatetime(cols=['birth', 'recruitmentDate', 'resignationDate'])
        p3 = processing.ApplyString(['id_'])
        p4 = processing.Filter(cols=['id_', 'name', 'birth', 'sex', 'recruitmentDate', 'resignationDate'])

        prc.add(p1)
        prc.add(p2)
        prc.add(p3)
        prc.add(p4)
        return prc


class AppointmentModel:

    def get_model(self):
        return SloadNProcessingModel(ILoader=self.get_loader(), IProcessing=self.get_processing())

    def get_loader(self):
        file_path = config.main_path.joinpath('4. 직원발령정보_22.5.12_test.csv')
        return loader.Loader(file_path=file_path)

    def get_processing(self):
        prc = processing.Composit()
        p1 = processing.Filter(cols=['사원', '사번', '발령일', '발령명', '소속부서', '직위', '직급', '직책', '비고'])
        p2 = processing.Sort(cols=['사번', '발령일'])
        p3 = processing.Rename(cols=['name', 'id_', 'ap_date', 'ap_name', 'ap_department', 'ap_position', 'ap_level', 'ap_leader_position', 'description'])
        p4 = processing.ApplyDatetime(cols=['ap_date'])
        p5 = processing.ApplyString(cols=['id_'])

        prc.add(p1)
        prc.add(p2)
        prc.add(p3)
        prc.add(p4)
        prc.add(p5)
        return prc

class AppointmentModel_v2:

    def get_model(self):
        return SloadNProcessingModel(ILoader=self.get_loader(), IProcessing=self.get_processing())

    def get_loader(self):
        file_path = config.main_path.joinpath('4. 직원발령정보_22.11.11_최신.csv')
        return loader.Loader(file_path=file_path)

    def get_processing(self):
        prc = processing.Composit()
        p1 = processing.Sort(cols=['사번', '발령일'])
        p2 = processing.Rename(cols=['name', 'id_', 'appointmentDate', 'appointmentName', 'department', 'workDepartment','position', 'level', 'leader', 'contractKind', 'appointmentDetail', 'reference'])
        p3 = processing.ApplyDatetime(cols=['appointmentDate'])
        p4 = processing.ApplyString(cols=['id_'])

        prc.add(p1)
        prc.add(p2)
        prc.add(p3)
        prc.add(p4)
        return prc

class DepartmentInfo:

    def get_model(self):
        return SloadNProcessingModel(ILoader=self.get_loader(), IProcessing=self.get_processing())

    def get_loader(self):
        file_path = config.main_path.joinpath('11. 직제정보.csv')
        return loader.Loader(file_path=file_path)

    def get_processing(self):
        prc = processing.Composit()
        p1 = processing.ApplyDatetime(cols=['start', 'end'])

        prc.add(p1)
        return prc