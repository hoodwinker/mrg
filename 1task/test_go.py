from pageobjects import selenium_driver
from pageobjects import page
import random
from datetime import datetime
from time import sleep

import pytest
base_url = "https://go.mail.ru/"

###########################################   FIXTURES   #######################

@pytest.yield_fixture(scope='module')
def module_setup():
    driver = selenium_driver.initialize(base_url)
    yield driver
    driver.quit()

@pytest.yield_fixture(scope='function')
def fucntion_setup():
    driver = selenium_driver.initialize(base_url)
    yield driver
    driver.quit()

@pytest.fixture(scope='function')
def main_page():
    main_page = page.MainPage()
    yield main_page
    main_page.close_suggest()

###########################################   TESTS   ##########################

@pytest.mark.usefixtures('module_setup')
@pytest.mark.parametrize("search_text", ['погода', 'температура'])
def test_suggest_weather(main_page, search_text):

    main_page.type_text(search_text, wait_for_suggest=True, clear_before_input=True)
    assert main_page.suggest_weather.is_here()
    

@pytest.mark.usefixtures('module_setup')
@pytest.mark.parametrize("search_text, result_text", [('вко', 'вконтакте'), ('поч', 'почта'), ('одн', 'одноклассники')])
def test_suggest_text(main_page, search_text, result_text):

    main_page.type_text(search_text, wait_for_suggest=True, clear_before_input=True)
    text_in_suggest = main_page.is_text_in_suggests(result_text, exact_match=True)
    assert text_in_suggest

@pytest.mark.usefixtures('module_setup')
@pytest.mark.parametrize("search_text", ['курс', 'доллар', 'евро'])
def test_suggest_currency(main_page, search_text):

    main_page.type_text(search_text, wait_for_suggest=True, clear_before_input=True)

    assert main_page.suggest_converter.is_here()
    # assert main_page.suggest_converter.get_text().find('ЦБ РФ') > -1

@pytest.mark.usefixtures('module_setup')
@pytest.mark.parametrize("search_text", ['унция', 'галлон', 'баррель'])
def test_suggest_converter(main_page, search_text):

    main_page.type_text(search_text, wait_for_suggest=True, clear_before_input=True)

    assert main_page.suggest_converter.is_here()

@pytest.mark.usefixtures('module_setup')
@pytest.mark.parametrize("search_text, result_text", [('ghbdtn', 'привет'), ('фшдюкг', 'mail.ru'), ('руддщ', 'hello')])
def test_suggest_layout(main_page, search_text, result_text):

    main_page.type_text(search_text, wait_for_suggest=True, clear_before_input=True)
    text_in_suggest = main_page.is_text_in_suggests(result_text, exact_match=True)

    assert text_in_suggest

@pytest.mark.usefixtures('module_setup')
@pytest.mark.parametrize("search_text, result_text", [('малоко', 'молоко'), ('курсдоллара', 'курс доллара'), ('фейс бук', 'фейсбук')])
def test_suggest_misprint(main_page, search_text, result_text):

    main_page.type_text(search_text, wait_for_suggest=True, clear_before_input=True)
    text_in_suggest = main_page.is_text_in_suggests(result_text, exact_match=False)

    assert text_in_suggest


@pytest.mark.skip(reason="missing in current version")
@pytest.mark.usefixtures('module_setup')
@pytest.mark.parametrize("search_text", ['рбк', 'википедия'])
def test_suggest_web(main_page, search_text, result_text):

    main_page.type_text(search_text, wait_for_suggest=True, clear_before_input=True)

    assert main_page.suggest_web.is_here()


@pytest.mark.usefixtures('module_setup')
@pytest.mark.parametrize("search_text", ['песня'])
def test_suggest_media(main_page, search_text):

    main_page.type_text(search_text, wait_for_suggest=True, clear_before_input=True)

    assert main_page.suggest_media.is_here()


@pytest.mark.skip(reason="missing in current version")
@pytest.mark.usefixtures('module_setup')
@pytest.mark.parametrize("search_text, search_old_text", [('регулярные выражения python', 'р')])
def test_suggest_old_query(main_page, search_text, search_old_text):
    main_page.type_text(search_text, wait_for_suggest=True, clear_before_input=True)
    main_page.search()
    
    sleep(30) #i'm not totally sure how suggestion in old searches works

    main_page.type_text(search_old_text, wait_for_suggest=True, clear_before_input=True)
    text_in_suggest = main_page.is_text_in_suggests(result_text, exact_match=False)

    assert text_in_suggest