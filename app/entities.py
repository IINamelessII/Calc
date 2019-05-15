from re import match


class CalcRequest():

    def __init__(self, string):
        self.string = string
    
    def calc(self):
        if self.is_expression:
            return 0

    @property
    def is_expression():
        return True
        