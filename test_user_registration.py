'''

    @Author: Shivraj Yelave
    @Date: 17-08-24
    @Last modified by: Shivraj Yelave
    @Last modified time: 19-08-24
    @Title: User Registration Unit Test


'''
import unittest  # Import the unittest module for creating and running tests.
import user_registration  # Import the user_registration module to test the functions.

class TestUserValidation(unittest.TestCase):
    """
    Description: 
    This class contains unit tests for validating the first name 
    using the 'valid_first_name' function from the 'user_registration' module.
    """

    def test_valid_first_name_case(self):
        """
        Description: 
        Test case for valid first names that should pass the validation.
        """
        # Valid names
        self.assertTrue(user_registration.valid_first_name("Shiv"))  # Should return True
        self.assertTrue(user_registration.valid_first_name("Prayag"))  # Should return True

    def test_invalid_first_name_case(self):
        """
        Description: 
        Test case for invalid first names that should fail the validation.
        """
        # Invalid names
        self.assertFalse(user_registration.valid_first_name("deven"))  # Should return False (starts with lowercase)
        self.assertFalse(user_registration.valid_first_name("ayush"))  # Should return False (starts with lowercase)
        self.assertFalse(user_registration.valid_first_name("Ay"))  # Should return False (too short)

    def test_is_last_name_valid(self):
        """
        Description: 
        Test case for invalid last names that should fail the validation.
        """
        self.assertTrue(user_registration.valid_last_name("Yelave"))  # Should return True
        self.assertTrue(user_registration.valid_last_name("Bhoir"))  # Should return True
        self.assertFalse(user_registration.valid_last_name("yelave"))  # Should return False
        self.assertFalse(user_registration.valid_last_name("Bo"))  # Should return False

    def test_is_email_valid(self):
        """
        Description: 
        Test case for validating email addresses that should pass or fail the validation.
        """
        # Valid email addresses
        self.assertTrue(user_registration.valid_email("shiv@yelave.com"))  # Should return True
        self.assertTrue(user_registration.valid_email("shiv.yelave123@gmail.co.in"))  # Should return True

        # Invalid email addresses
        self.assertFalse(user_registration.valid_email("shiv@.com"))  # Should return False (no domain name)
        self.assertFalse(user_registration.valid_email("shiv@gmail"))  # Should return False (no top-level domain)
        self.assertFalse(user_registration.valid_email("shiv@yelave,com"))  # Should return False (invalid character in domain)

if __name__ == "__main__":
    unittest.main()  # Run the tests when the script is executed directly.
