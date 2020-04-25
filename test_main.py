import unittest
from unittest.mock import patch, mock_open
import main

password = "s0m3%P4$$wD"

# START TESTS
class Test(unittest.TestCase):

    def test_parse_args_short_arg(self):
        args = main.parse_args(["-p", password])
        self.assertEqual(args.password, password)

    def test_parse_args_long_arg(self):
        args = main.parse_args(["--password", password])
        self.assertEqual(args.password, password)        

    def test_parse_args_with_invalid_args(self):
        with self.assertRaises(SystemExit): main.parse_args(["-x", "y"])
    
    """
    Test acceptable password
    """
    def test_validate_password(self):
        self.assertEqual(main.validate_password(password), True)
        self.assertEqual(main.validate_password("azAZ09#"), True)
        self.assertEqual(main.validate_password("azAZ09%"), True)
        self.assertEqual(main.validate_password("azAZ09$"), True)
        self.assertEqual(main.validate_password("azAZ09#%$"), True)

    """
    Test not acceptable password
    """
    def test_validate_password_fail(self):
        self.assertEqual(main.validate_password("az"), False)
        self.assertEqual(main.validate_password("azAZ"), False)
        self.assertEqual(main.validate_password("azAZ09"), False)
        self.assertEqual(main.validate_password("aA0#"), False)
        self.assertEqual(main.validate_password("xyzXYZ123#%$0"), False)
        


unittest.main()
