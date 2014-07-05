from django.test import TestCase

from templatetags.tagslim import ntimes


class Test_ntimes(TestCase):
    def test_length(self):
        expected = 5
        actual = len(ntimes(5))
        self.assertEquals(expected, actual)
