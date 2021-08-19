import unittest
import sys
from common.basepage import BasePage
from common.read_config_utils import Config
from common.browser import Browser

class SeleniumBase(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.url = Config.get_config_url

    def setUp(self) -> None:
        self.basepage = BasePage(Browser().get_driver())
        self.basepage.wait()
        self.basepage.open_url(self.url)
        self.basepage.max_browser()

    def tearDown(self) -> None:
        self.basepage.quit_browser()
