import testtools


class DummyTestCase(testtools.TestCase):

    def setUp(self):
        super(DummyTestCase, self).setUp()

    def test_dummy(self):
        self.assertEqual(2+2, 4)
