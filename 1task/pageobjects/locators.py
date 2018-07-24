from selenium.webdriver.common.by import By


class MainPageLocators(object):
    """A class for main page locators.
    All main page locators should come here"""
    SEARCH_LINE = (By.NAME, 'q')
    SUGGEST_WRAP = (By.XPATH, '//*[@class="go-suggests__helpwrap"]')
    suggest_text = (By.XPATH, '//*[@class="go-suggests__item__text"]')
    suggest_weather = (By.XPATH, '//*[@class="go-suggests__item__weather go-suggests__item__weather-ico"]')
    suggest_converter = (By.XPATH, '//*[@class="go-suggests__item__converter"]')
    suggest_media = (By.XPATH, '//*[@class="go-suggests__item__musico"]')
    suggest_web = (By.XPATH, '') #
    spacer = (By.XPATH, '//*[@class="js-spacer pm-toolbar__spacer  pm-toolbar__spacer_first pm-toolbar__spacer_flexible"]')