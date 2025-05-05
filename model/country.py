from dataclasses import dataclass


@dataclass
class Country:
    StateAbb:str
    CCode:str
    StateNme:str

    def __eq__(self, other):
        return self.CCode==other.CCcode

    def __lt__(self, other):
        return self.StateNme<other.StateNme
    def __hash__(self):
        return hash(self.CCode)