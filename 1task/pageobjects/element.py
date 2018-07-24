from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import contextlib

class SuggestPageElement(object):
    def get_text(self):
        element = self.driver.find_element(*self.locator)
        return element.text

    def get_value(self):
        element = self.driver.find_element(*self.locator)
        return element.get_attribute("value")


class FloatingPageElement(object):
    pass


class BasePageElement(object):
    def click(self):
        element = self.driver.find_element(*self.locator)
        element.click()

    def focus(self):
        driver = self.driver
        WebDriverWait(driver, 100).until(
            lambda driver: driver.find_element(*self.locator))
        driver.find_element(*self.locator).send_keys(Keys.NULL)

    def wait(self, time=30):
        wait = WebDriverWait(self.driver, time)
        wait.until(EC.visibility_of_element_located(self.locator))

    @contextlib.contextmanager
    def wait_for_page_load(self, time=10):
        driver = self.driver
        old_page = driver.find_element_by_tag_name('html')
        yield
        WebDriverWait(driver, time).until(EC.staleness_of(old_page))

    def is_here(self):
        try:
            self.driver.find_element(*self.locator)
        except NoSuchElementException:
            return False
        return True

    def press_Enter(self):
        element = self.driver.find_element(*self.locator)
        element.send_keys(Keys.ENTER)


class MultiplePageElement(object):

    def click_from_list(self, row):
        el_arr = self.driver.find_elements(*self.locator)
        el_arr[row].click()

    def get_all_list(self):
        el_arr = self.driver.find_elements(*self.locator)
        return len(el_arr)

    def list_of_all_elem(self):
        el_arr = self.driver.find_elements(*self.locator)
        for el in el_arr:
            yield el


class TextPageElement(object):

    def set_text(self, value, clear=False, gotostart=False):
        driver = self.driver
        element = driver.find_element(*self.locator)
        if clear:
            element.clear()
        if gotostart:
            element.send_keys(Keys.CONTROL, Keys.HOME)
        element.send_keys(value)