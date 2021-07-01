import os
import configparser

current_path = os.path.dirname(__file__)
config_path = os.path.join(current_path, '../conf/config.ini')
class ReadconfigUtils(object):
    def __init__(self,config_path=config_path):
        self.config = configparser.ConfigParser()
        self.config.read(config_path,encoding='utf-8')

    @property
    def get_config_url(self):
        value = self.config.get('default','url')
        return value

    @property
    def get_driver(self):
        value = self.config.get('default','driver_type')
        return value

    @property
    def get_driver_path(self):
        value = self.config.get('default', 'driver_path')
        return value

    @property
    def get_timeout(self):
        value = self.config.get('default', 'timeout')
        return value

    @property
    def get_screentshot_path(self):
        value = self.config.get('default', 'screentshop_path')
        return value

    @property
    def get_username(self):
        value = self.config.get('default', 'username')
        return value

    @property
    def get_password(self):
        value = self.config.get('default', 'password')
        return value

    @property
    def test_data_path(self):
        value = self.config.get('default', 'test_data_path')
        return value

    @property
    def email_smtp_server(self):
        value = self.config.get('email', 'smtp_server')
        return value

    @property
    def email_smtp_sender(self):
        value = self.config.get('email', 'smtp_sender')
        return value

    @property
    def email_smtp_password(self):
        value = self.config.get('email', 'smtp_password')
        return value

    @property
    def email_smtp_receiver(self):
        value = self.config.get('email', 'smtp_receiver')
        return value

    @property
    def email_smtp_cc(self):
        value = self.config.get('email', 'smtp_cc')
        return value

    @property
    def email_smtp_subject(self):
        value = self.config.get('email', 'smtp_subject')
        return value

Config = ReadconfigUtils()
if __name__=='__main__':
    print(Config.email_smtp_cc)