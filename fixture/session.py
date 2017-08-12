class SessionHelper:

    def __init__(self, app):
        self.app = app

    def login(self, username, password):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath(".//*[@id='LoginForm']/input[@value='Login']").click()

    def logout(self) -> object:
        wd = self.app.wd
        wd.find_element_by_link_text("Logout").click()