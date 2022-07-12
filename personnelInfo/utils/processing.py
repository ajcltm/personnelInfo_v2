from typing_extensions import Protocol
from typing import List
import pandas as pd

class IProcessing(Protocol):

    def processing(self):
        ...


class Rename:

    def __init__(self, cols:List) -> None:
        self.cols = cols

    def processing(self, df:pd.DataFrame) -> pd.DataFrame:
        df.columns = self.cols
        return df


class ApplyDatetime:

    def __init__(self, cols:List) -> None:
        self.cols = cols
    
    def processing(self, df:pd.DataFrame) -> pd.DataFrame:
        for col in self.cols:
            df[col] = pd.to_datetime(df[col], format='%Y-%m-%d')
        return df


class ApplyString:

    def __init__(self, cols:List) -> None:
        self.cols = cols

    def processing(self, df:pd.DataFrame) -> pd.DataFrame:
        for col in self.cols:
            df[col] = df[col].apply(lambda x: str(int(x)))
        return df


class Filter:
    def __init__(self, cols:List) -> None:
        self.cols = cols

    def processing(self, df:pd.DataFrame) -> pd.DataFrame:
        return df[self.cols]


class Sort:
    def __init__(self, cols:List) -> None:
        self.cols = cols

    def processing(self, df:pd.DataFrame) -> pd.DataFrame:
        return df.sort_values(by=self.cols)


class Composit:

    def __init__(self):
        self.processingList = []

    def add(self, processing:IProcessing) -> None:
        self.processingList.append(processing)

    def processing(self, df:pd.DataFrame) -> pd.DataFrame:
        _df = df
        for i in self.processingList:
            _df = i.processing(_df)
        return _df
