import unittest
import sys
import logging


class MainTest(unittest.TestCase):

    def setUp(self):
        sys.stdout.flush()
        logging.info("This is setup")
        print "\nThis is setup method"

    def tearDown(self):
        logging.info("this is tear")
        print "This is tear down method"

    def test_1(self):
        logging.info("this is test")
        print "This is first test"
