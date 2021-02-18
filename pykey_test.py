import unittest
import pykey

class TestUser (unittest.TestCase):

    def setUpClass(self):
        print("Setting up class")

    def tearDownClass(self):
        print("Tearing down class")

    def setUp(self):
        print("Set up")
        self.user1 = User


