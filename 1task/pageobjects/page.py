from pageobjects.element import BasePageElement, SuggestPageElement, TextPageElement, MultiplePageElement, FloatingPageElement
from pageobjects.locators import MainPageLocators
from pageobjects import selenium_driver


class TextElement(BasePageElement, TextPageElement):

    def __init__(self, *locator):
        self.locator = locator
        self.driver = selenium_driver.driver

class SuggestElement(BasePageElement, SuggestPageElement, MultiplePageElement):

    def __init__(self, *locator):
        self.locator = locator
        self.driver = selenium_driver.driver

class FloatingElement(BasePageElement, FloatingPageElement):

    def __init__(self, *locator):
        self.locator = locator
        self.driver = selenium_driver.driver

class BasePage(object):
    """Base class to initialize the base
    page that will be called from all pages"""

    def __init__(self):
        self.driver = selenium_driver.driver


class MainPage(BasePage):
    """Home page action methods come here."""
    
    def __init__(self):
        super().__init__()

        self.SEARCH_LINE = TextElement(*MainPageLocators.SEARCH_LINE)
        self.SUGGEST_WRAP = FloatingElement(*MainPageLocators.SUGGEST_WRAP)
        
        self.suggest_text = SuggestElement(*MainPageLocators.suggest_text)
        self.suggest_weather = SuggestElement(*MainPageLocators.suggest_weather)
        self.suggest_converter = SuggestElement(*MainPageLocators.suggest_converter)
        self.suggest_media = SuggestElement(*MainPageLocators.suggest_media)
        self.suggest_web = SuggestElement(*MainPageLocators.suggest_web)
        self.suggest_text = SuggestElement(*MainPageLocators.suggest_text)
        
    def close_suggest(self):
        spacer = FloatingElement(*MainPageLocators.spacer)
        spacer.click()

    def search(self):
        element = self.SEARCH_LINE
        element.press_Enter()

    def type_text(self, text, wait_for_suggest, clear_before_input, go_to_start=False):
        self.SEARCH_LINE.set_text(text, clear=clear_before_input, gotostart=go_to_start)
        if wait_for_suggest:
            self.SUGGEST_WRAP.wait()

    def is_text_in_suggests(self, search_text, exact_match):
        text_elem = self.suggest_text
        for sugg_elem in text_elem.list_of_all_elem():
            if exact_match:
                if sugg_elem.text == search_text:
                    return True
            else:
                if sugg_elem.text.find(search_text) > -1:
                    return True
        else:
            return False
