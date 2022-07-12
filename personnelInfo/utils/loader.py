from typing_extensions import Protocol
import pandas as pd

class ILoader(Protocol):

    def load(self):
        ...


class Loader:

    def __init__(self, file_path):
        self.file_path = file_path

    def load(self):
        return pd.read_csv(self.file_path, encoding='utf-8')