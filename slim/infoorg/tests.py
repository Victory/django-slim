from selenium import webdriver
from time import sleep

from django.test import LiveServerTestCase

from django.contrib.staticfiles.testing \
    import StaticLiveServerCase


class LiveValidationTestCase(StaticLiveServerCase):
    """
    run tests on ajaxy live validation
    """

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_homepage_200(self):
        self.browser.get(self.live_server_url + "/infoorg/")
        assert "Welcome to info home" in self.browser.page_source


class InfoTipFormTestCase(StaticLiveServerCase):
    def key(self, name, txt):
        selector = "[name=" + name + "]"
        elm = self.browser.find_element_by_css_selector(selector)
        elm.send_keys(txt)

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_submit_info_tip(self):
        self.browser.get(self.live_server_url + "/infoorg/")
        form = self.browser.find_element_by_id("infoTipForm")
        self.key("subject", "just some text")
        self.key("message", "just some other text")
        self.key("sender", "just@nemail.com")
        form.find_element_by_css_selector("[type=submit]").click()
        assert self.browser.current_url == self.live_server_url + "/infoorg/"
        sleep(1)
        formBox = self.browser.find_element_by_id("formBox")
        assert formBox.text == "Thanks for Submitting!"

    def test_submit_info_tip_with_error(self):
        self.browser.get(self.live_server_url + "/infoorg/")
        form = self.browser.find_element_by_id("infoTipForm")
        self.key("subject", "just some text")
        self.key("message", "just some other text")

        form.find_element_by_css_selector("[type=submit]").click()
        assert self.browser.current_url == self.live_server_url + "/infoorg/"
        sleep(1)
        errs = self.browser.find_elements_by_css_selector(".errorlist")
        assert len(errs) > 0

        self.key("sender", "just@nemail.com")
        form = self.browser.find_element_by_id("infoTipForm")
        form.find_element_by_css_selector("[type=submit]").click()
        sleep(1)
        formBox = self.browser.find_element_by_id("formBox")
        assert formBox.text == "Thanks for Submitting!"
