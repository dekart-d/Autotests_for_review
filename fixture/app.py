#SetUp&TearDown и опции браузера, тут запускается хедлесс, и если надо для отладки тестов отключается
from selenium import webdriver


class application:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.headless = True
        chrome_options.add_argument("--disable-extensions")
        chrome_options.add_argument('window-size=1920x1080')
        chrome_options.add_argument('- disable-gpu')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument('--enable-javascript')
        chrome_options.add_argument('--ignore-certificate-errors')
        chrome_options.add_argument('--disable-dev-shm-usage')
        # chrome_options.add_argument('--auto-open-devtools-for-tabs')
        self.driver = webdriver.Chrome(options=chrome_options) #options=chrome_options
        self.driver.delete_all_cookies()
        self.driver.implicitly_wait(2)



    def open_form(self, url: str):
        driver = self.driver
        driver.get(url)


    def destroy(self):
        self.driver.quit()
