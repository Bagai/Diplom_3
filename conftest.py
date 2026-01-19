from selenium.webdriver.chrome.options import Options

# from selenium.webdriver.firefox.options import Options

from selenium import webdriver
import pytest


@pytest.fixture  # (params=["Chrome"])  # , "Firefox"])
def driver():  # request):
    options = Options()
    options.add_argument("--window-size=1920x1080")
    # if request.param == "Chrome":
    # driver = webdriver.Chrome(options=options)
    # else:
    #     driver = webdriver.Firefox(options=options)
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()
