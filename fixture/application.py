# -*- coding: utf-8 -*-

from selenium import webdriver
from fixture.session import SessionHelper


class Application:

    def __init__(self, browser, web_config):
        if browser == "chrome":
            self.wd = webdriver.Chrome()
            self.wd.maximize_window()
        elif browser == "firefox":
            self.wd = webdriver.Firefox()
            self.wd.maximize_window()
        else:
            raise ValueError("Unrecognized browser %s" % browser)
        self.wd.implicitly_wait(2)
        self.session = SessionHelper(self, web_config)

    def destroy(self):
        self.wd.quit()
