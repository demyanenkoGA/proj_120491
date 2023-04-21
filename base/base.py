import datetime


class Base:
    def __init__(self, driver):
        self.driver = driver

    def get_current_url(self):
        """Method get current URL"""
        get_url = self.driver.current_url
        print(f'Current url {get_url}')

    def assert_word(self, word, result):
        """Method assert word"""
        value_word = word.text
        assert value_word == result
        print("Good value word")

    def assert_url(self, result):
        """Method assert url"""
        get_url = self.driver.current_url
        assert get_url == result
        print("Good value url")

    def get_screenshot(self):
        """Method screenshot"""
        now_datetime = datetime.datetime.utcnow().strftime("%Y.%m.%d_%H.%M.%S")
        name_screenshot = f'./screen/SCREENSHOT_{now_datetime}.png'
        self.driver.save_screenshot(name_screenshot)
