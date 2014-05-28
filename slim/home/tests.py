from selenium import webdriver

from django.test import LiveServerTestCase


class LiveValidationTestCase(LiveServerTestCase):
    """
    run tests on ajaxy live validation
    """

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_homepage_200(self):
        self.browser.get(self.live_server_url)
        assert "HELLO SLIM" in self.browser.title
