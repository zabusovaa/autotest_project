from .base_page import BasePage
from .locators import LoginPageLocators
from .locators import MainPageLocators


class LoginPage(BasePage):
    def register_new_user(self, email, password):
        reg_email = self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL)
        reg_email.send_keys(email)
        reg_pass1 = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD1)
        reg_pass1.send_keys(password)
        reg_pass2 = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD2)
        reg_pass2.send_keys(password)
        reg_btn = self.browser.find_element(*LoginPageLocators.REGISTER_BTN)
        reg_btn.click()

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # проверка на корректный url адрес
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()
        assert "login" in self.browser.current_url, "Некорректный url, 'login' отсутствует"

    def should_be_login_form(self):
        # проверка, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Форма входа отсутствует"


    def should_be_register_form(self):
        # проверка, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Форма регистрации отсутствует"
