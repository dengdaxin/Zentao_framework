from common.element_info_utils import ElementUtils
def get_isnot(mudule_name,case_name):
    element = ElementUtils('login_suite',mudule_name).get_elements_info()
    value = element[case_name]
    isnot = value['isnot']
    return isnot