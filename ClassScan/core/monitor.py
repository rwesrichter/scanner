import os
import pandas as pd
import ClassScan
from ClassScan.core.client import sms, call

config = ClassScan.get_config()

class monitor:
    __slots__ = ['user', 'device', 'listen', 'inbox', 'student_df', 'sms', 'call']
    def __init__(self):
        self.user = {'ID': config.get('USER', 'ID'),
                     'FIRST': config.get('USER', 'FIRST'),
                     'LAST': config.get('USER', 'LAST'),
                     'ROOM_NUMBER': config.get('USER', 'ROOM'),
                     'PHONE_NUMBER': config.get('USER', 'NUMBER')}
        self.student_df = None
        self.sms = sms()
        self.call = call()
        self.preprocess()

    def preprocess_students(self):
        path = os.path.join(ClassScan.DATA_DIR, 'ClassStudentListingwithAddresses.xlsx')
        df = pd.read_excel(path, skiprows=1)
        df = df.set_index('Student Local ID')
        self.student_df = df

    def preprocess(self):
        self.preprocess_students()

    def input_menu(self):
        ptype = input("Pass Type: ")
        return ptype

    def input_id(self):
        ptype = input("Id: ")
        try:
            ptype = int(ptype)
        except AttributeError:
            return False
        return ptype

    @staticmethod
    def process_type(ptype):
        try:
            pass_code = ClassScan.pass_dict[ptype]
        except KeyError:
            print('Not Valid Type')
            pass_code = 0
        return pass_code

    def process_id(self, input_id):
        if input_id == int(config.get('USER', 'ID')):
            return self.user
        try:
            student = self.student_df.loc[input_id]
        except KeyError:
            print('Student Not Found')  # we need to probably add this student
            return False
        return student

    def issue(self, individual, code):
        message = f'You have been issued a {code} pass'
        self.sms.message(message, individual['PHONE_NUMBER'])

    def process(self):
        """
        - Input menu
        - Process Pass Type
        - Input Id
        - Process Id
        - Issue Pass
        :return: sms containing picture hall pass
        """
        #  Input/Process Menu
        ptype = self.input_menu()
        pass_code = self.process_type(ptype)

        #  Input/Process Id
        id = self.input_id()
        individual = self.process_id(id)

        #  Issue Pass
        self.issue(individual, pass_code)



