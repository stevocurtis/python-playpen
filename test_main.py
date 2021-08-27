import unittest
import main


class TestMain(unittest.TestCase):
    def testRun(self):
        self.assertEqual(main.run(), "hello world")
