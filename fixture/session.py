# -*- coding: utf-8 -*-

import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC


class SessionHelper:

    def __init__(self, app, web_config):
        self.app = app
        self.web_config = web_config

    def open_home_page(self):
        wd = self.app.wd
        base_url = self.web_config['baseUrl']
        if wd.current_url != base_url:
            wd.get(base_url)
            time.sleep(2)

    def entry_to_email(self):
        wd = self.app.wd
        entry_list = wd.find_elements_by_link_text("Войти в почту")
        if len(entry_list) > 0:
            entry_list[0].click()
            time.sleep(2)

    def setvalue(self, value, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_id(value).click()
            wd.find_element_by_id(value).clear()
            wd.find_element_by_id(value).send_keys(text)

    def input_username(self, username):
        wd = self.app.wd
        if username is not None:
            if wd.find_elements_by_tag_name('label')[0].text == "Введите логин, почту или телефон":
                self.setvalue("passp-field-login", username)
                wd.find_element_by_css_selector('button[type="submit"]').click()

    def input_password(self, password):
        wd = self.app.wd
        if password is not None:
            if wd.find_elements_by_tag_name('label')[0].text == "Введите пароль":
                self.setvalue("passp-field-passwd", password)
                wd.find_element_by_css_selector('button[type="submit"]').click()

    def logout(self):
        wd = self.app.wd
        mainmenu = wd.find_elements_by_class_name("mail-User-Name")
        if (len(mainmenu) == 1) and (mainmenu[0].text == self.web_config['username']):
            mainmenu[0].click()
            submenu = Wait(wd, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "Выйти из сервисов Яндекса")))
            submenu.click()
        else:
            raise Warning("More than one element")

    # Достаточно проверить наличие двух папок "Входящие" и "Отправленные"
    def check_email_folders(self):
        wd = self.app.wd
        inbox = False
        sent = False
        wait_folders = Wait(wd, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "span.js-folders-item-name")))
        folders_list = wd.find_elements_by_css_selector("span.js-folders-item-name")
        for item in folders_list:
            if item.text == "Входящие":
                inbox = True
            if item.text == "Отправленные":
                sent = True

        if inbox and sent:
            return True
        else:
            return False

    def get_element(self):
        wd = self.app.wd
        element = wd.find_element_by_class_name("passp-form-field__error").text
        return element
