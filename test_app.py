import app
import unittest
import xmlrunner

class TestFunction1(unittest.TestCase):
  """
  Functional testing the app
  """

  def test_function1a(self):
    """
    testing function1 with a variables
    """
    result=3
    self.assertEqual(result,3)

  def test_function1b(self):
    """
    testing with b variabls
    """
    result=3
    self.assertEqual(result,2)

if __name__ == '__main__':
  unittest.main(testRunner=xmlrunner.XMLTestRunner(output="./python_unittests_xml"))

