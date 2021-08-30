from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
def init_driver(headless = True):
    '''Start chrome driver using webdriver_manager which downloads perfet version of chrome executables w.r.t your Chrome Browser.'''
    if headless:
        # Basic required arguments are already added for smooth working in headless mode
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-notifications")
        chrome_options.add_argument("--log-level=3")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--disable-features=NetworkService")
        chrome_options.add_argument("--disable-software-rasterizer")
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument("--disable-popup-blocking")
        chrome_options.add_argument("--start-maximized")
        return webdriver.Chrome(ChromeDriverManager().install(),chrome_options=chrome_options)

    else:
        return webdriver.Chrome(ChromeDriverManager().install())
