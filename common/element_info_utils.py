import os
import xlrd

current_path = os.path.dirname(__file__)
excel_path = os.path.join(current_path, '../element_data/element_infos.xlsx')

class ElementUtils:
    def __init__(self,sheet_name,module_name,excel_path=excel_path):
        '''page_name是sheet的名称'''
        self.excel_path = excel_path
        self.workbook = xlrd.open_workbook(self.excel_path)
        self.sheet = self.workbook.sheet_by_name(sheet_name)
        self.module_name = module_name
    def get_elements_info(self):
        element_infos = {}
        for i in range(1,self.sheet.nrows):
            if self.module_name == self.sheet.cell_value(i,2):
                element = {}
                element['element_name'] = self.sheet.cell_value(i,1)
                element['element_type'] = self.sheet.cell_value(i,3)
                element['element_value'] = self.sheet.cell_value(i,4)
                element['timeout'] = self.sheet.cell_value(i,5)
                element_infos[self.sheet.cell_value(i,0)] = element
        return element_infos

if __name__=='__main__':
    element = ElementUtils('login_suite','login')
    elem = element.get_elements_info()
    for i in elem.items():
        print(i)

