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
def main():
    """
    Description: 
    Main function to handle user input and validate the first name.
    Logs the result of the validation.
    """
    user_first_name = 'Shiv'  # Description: Prompt the user to enter their first name.
    user_last_name = 'Yelave'  # Description: Prompt the user to enter their first name.
    user_email = 'shivyelave@gmail.ac.com'  # Description: Prompt the user to enter their email.
    user_number = '9999999999'  # Description: Prompt the user to enter their email.


    first_name_result = valid_first_name(user_first_name)  # Description: Validate the entered first name.
    last_name_result = valid_first_name(user_first_name)  # Description: Validate the entered first name.
    email_result = valid_email(user_email)  # Description: Validate the entered email.
    number_result = valid_mobile_number(user_number)  # Description: Validate the entered email.


    info_logger = get_info_logger(__name__)  # Description: Get an info-level logger instance.


    if first_name_result:
        # Description: Log a message if the first name is valid.
        info_logger.info(f'First Name {user_first_name} is Valid')
    else:
        # Description: Log a message if the first name is invalid.
        info_logger.info(f'First Name {user_first_name} is Invalid')     



    if last_name_result:
        # Description: Log a message if the last name is valid.
        info_logger.info(f'Last Name {user_last_name} is Valid')
    else:
        # Description: Log a message if the last name is invalid.
        info_logger.info(f'Last Name {user_last_name} is Invalid')   

    if email_result:
        # Description: Log a message if the email is valid.
        info_logger.info(f'Email {user_email} is Valid')
    else:
        # Description: Log a message if the email is invalid.
        info_logger.info(f'Email {user_email} is Invalid') 


    if number_result:
        # Description: Log a message if the number is valid.
        info_logger.info(f'Number {user_number} is Valid')
    else:
        # Description: Log a message if the number is invalid.
        info_logger.info(f'Number {user_number} is Invalid') 

if __name__ == '__main__':
    main()  # Description: Execute the main function if the script is run directly.
