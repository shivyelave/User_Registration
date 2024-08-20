'''

    @Author: Shivraj Yelave
    @Date: 17-08-24
    @Last modified by: Shivraj Yelave
    @Last modified time: 20-08-24
    @Title: User Registration


'''

# Import required modules
import sys
import os
import re

# Add the path to the plotly directory
sys.path.append(os.path.abspath('C:/Users/Admin/Documents/Python Basics'))

# Import the logger functions from the logger module
from logger import (get_info_logger) 

def valid_first_name(first_name):
    """
    Description: 
    Validates the first name based on the defined format.

    Parameters:
    first_name (str): The first name entered by the user.

    Returns:
    bool: True if the name matches the format, False otherwise.
    """
    valid_name_format = r'^[A-Z][a-zA-z]{2,}$'  # Description: Regex pattern to ensure the name starts with an uppercase letter and has at least 3 letters.
    return re.match(valid_name_format, first_name)  # Description: Match the input name with the regex pattern.

def valid_last_name(last_name):
    """
    Description: 
    Validates the/ last name based on the defined format.

    Parameters:
    last_name (str): The last name entered by the user.

    Returns:
    bool: True if the name matches the format, False otherwise.
    """
    valid_name_format = r'^[A-Z][a-zA-z]{2,}$'  # Description: Regex pattern to ensure the name starts with an uppercase letter and has at least 3 letters.
    return re.match(valid_name_format, last_name)  # Description: Match the input name with the regex pattern.
def valid_email(email):
    """
    Description:
    Validates the email address based on the defined format.

    Parameters:
    email (str): The email address entered by the user.

    Returns:
    bool: True if the email matches the format, False otherwise.
    """
    # Description: Regex pattern to validate email addresses
    valid_email_format = r'^[a-zA-Z0-9]+[\.a-zA-Z0-9]*@[a-zA-Z0-9]+[\.a-zA-Z]*\.[a-zA-z]{2,}$'
    
    # Description: Match the input email with the regex pattern
    return re.match(valid_email_format, email)
def valid_mobile_number(mobile_number):
    """
    Description:
    Validates the mobile number based on the defined format.

    Parameters:
    mobile_number (str): The mobile number entered by the user.

    Returns:
    bool: True if the mobile number matches the format, False otherwise.
    """
    # Description: Regex pattern to validate the mobile number
    valid_mobile_format = r'^\d{10}$'
    
    # Description: Match the input mobile number with the regex pattern
    return re.match(valid_mobile_format, mobile_number)

def valid_password(password):
    """
    Description:
    Validates the password based on the rule of having a minimum of 8 characters.

    Parameters:
    password (str): The password entered by the user.

    Returns:
    bool: True if the password is at least 8 characters long, False otherwise.
    """
    # Description: Regex pattern to validate minimum length of 8 characters
    valid_password_format = r'^(?=.*[A-Z])(?=.*\d)(?=.*[\W_])(?!.*[\W_].*[\W_]).{8,}$'

    
    # Description: Match the input password with the regex pattern
    return re.match(valid_password_format, password)

def main():
    """
    Description: 
    Main function to handle user input and validate the first name, last name, email, mobile number, and password.
    Logs the result of the validation.
    """
    info_logger = get_info_logger(__name__)  # Description: Get an info-level logger instance.

    # Validate first name
    while True:
        # Description: Prompt the user to enter their first name.
        user_first_name = input("Enter your first name: ")
        # Description: Validate the entered first name.
        first_name_result = valid_first_name(user_first_name)
        if first_name_result:
            # Description: Log a message if the first name is valid.
            info_logger.info(f'First Name {user_first_name} is Valid')
            break
        else:
            # Description: Log a message if the first name is invalid.
            info_logger.info(f'First Name {user_first_name} is Invalid')
            print("Invalid first name. Please try again.")

    # Validate last name
    while True:
        # Description: Prompt the user to enter their last name.
        user_last_name = input("Enter your last name: ")
        # Description: Validate the entered last name.
        last_name_result = valid_last_name(user_last_name) 
        if last_name_result:
            # Description: Log a message if the last name is valid.
            info_logger.info(f'Last Name {user_last_name} is Valid')
            break
        else:
            # Description: Log a message if the last name is invalid.
            info_logger.info(f'Last Name {user_last_name} is Invalid')
            print("Invalid last name. Please try again.")

    # Validate email
    while True:
        # Description: Prompt the user to enter their email.
        user_email = input("Enter your email: ")
        # Description: Validate the entered email.
        email_result = valid_email(user_email)
        if email_result:
            # Description: Log a message if the email is valid.
            info_logger.info(f'Email {user_email} is Valid')
            break
        else:
            # Description: Log a message if the email is invalid.
            info_logger.info(f'Email {user_email} is Invalid')
            print("Invalid email. Please try again.")

    # Validate mobile number
    while True:
        # Description: Prompt the user to enter their mobile number.
        user_number = input("Enter your mobile number: ")
        # Description: Validate the entered mobile number.
        number_result = valid_mobile_number(user_number)
        if number_result:
            # Description: Log a message if the number is valid.
            info_logger.info(f'Number {user_number} is Valid')
            break
        else:
            # Description: Log a message if the number is invalid.
            info_logger.info(f'Number {user_number} is Invalid')
            print("Invalid mobile number. Please try again.")

    # Validate password
    while True:
        # Description: Prompt the user to enter their password.
        user_password = input("Enter your password: ")
        # Description: Validate the entered password.
        password_result = valid_password(user_password)
        if password_result:
            # Description: Log a message if the password is valid.
            info_logger.info(f'Password is Valid')
            break
        else:
            # Description: Log a message if the password is invalid.
            info_logger.info(f'Password is Invalid')
            print("Invalid password. Please try again.")

        


if __name__ == '__main__':
    main()  # Description: Execute the main function if the script is run directly.
