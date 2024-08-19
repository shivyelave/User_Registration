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

if __name__ == "__main__":
    unittest.main()  # Run the tests when the script is executed directly.
