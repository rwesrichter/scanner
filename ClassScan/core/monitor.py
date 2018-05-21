import os
import pandas as pd
import ClassScan

config = ClassScan.get_config()

class monitor:
    def _init__(self):
        self.device = None
        self.listen = None
        self.inbox = None
        self.student_df = None
        self.preprocess()

    def display_menu(self):
        ptype = input("Pass Type:")
        return ptype

    @staticmethod
    def process_type(ptype):
        try:
            pass_code = ClassScan.pass_dict[ptype]
        except KeyError:
            print('Not Valid Type')
            pass_code = 0
        return pass_code

    @staticmethod
    def process_individual(id):
        pass

    def preprocess_students(self):
        path = os.path.join(ClassScan.DATA_DIR, 'ClassStudentListingwithAddresses')
        df = pd.read_excel('ClassStudentListingwithAddresses')
        self.student_df = df

    def preprocess(self):
        self.preprocess_students()

    def process(self):
        ptype = self.display_menu()
        code = self.process_type(ptype)




