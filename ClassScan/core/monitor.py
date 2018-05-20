import ClassScan

class monitor:
    def _init__(self):
        self.device = None
        self.listen = None
        self.inbox = None
        self.student_df = None
        self.teacher_df = None

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
    
    def process(self):
        ptype = self.display_menu()
        code = self.process_type(ptype)




