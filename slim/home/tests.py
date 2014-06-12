from selenium import webdriver

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
        self.browser.get(self.live_server_url)
        assert "HELLO SLIM" in self.browser.title


class LiveStaticTestCase(StaticLiveServerCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_jquery_200(self):
        self.browser.get(self.live_server_url + "/static/js/jquery.js")

    def test_footer(self):
        self.browser.get(self.live_server_url)
        footer = self.browser.find_element_by_id("footTag")
        assert footer.text == u"footer"
