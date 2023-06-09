import pytest
from selene import browser, have, be


@pytest.fixture
def browser_size_window():
    browser.config.window_width = 1360
    browser.config.window_height = 768


@pytest.fixture
def open_browser_link():
    browser.open('https://google.com')


def test_successful_find_selene(open_browser_link, browser_size_window):
    browser.element('[name="q"]').should(be.blank).type('selene').press_enter()
    browser.element('[id="search"]').should(have.text('User-oriented Web UI browser tests in Python'))


def test_unsuccessful_find_selene(open_browser_link, browser_size_window):
    browser.element('[name="q"]').should(be.blank).type('asldksal;dkas;dlka;sldka;sdk;lsadkas;ld').press_enter()
    assert browser.element('[id="result-stats"]').should(have.text('Результатов: примерно 0'))
