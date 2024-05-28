from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

class AdminPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.menu_options = {
            "User Management": (By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[1]/span'),
            "Job": (By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[2]/span'),
            "Organization": (By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[3]/span'),
            "Qualifications": (By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[4]/span'),
            "Nationalities": (By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[5]/a'),
            "Corporate Banking": (By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[6]/a'),
            "Configuration": (By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[7]/span')
        }

    def click_menu_option(self, option_name: str):
        try:
            self.driver.find_element(*self.menu_options[option_name]).click()
        except Exception as e:
            print(f"An error occurred while clicking {option_name}: {e}")
