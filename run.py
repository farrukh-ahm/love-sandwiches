import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file("creds.json")
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("love_sandwiches")


def get_sales_data():
    """
    Get sales figure input from the user.
    """
    while True:
        print("Please enter sales data fromt the last market")
        print("Data should be six numbers, separated by commas")
        print("Example: 8,12,5,78,15,23")
        data_str = input("Enter your data here: ")
        sales_data = data_str.split(",")
        
        if validate_data(sales_data):
            print("Validated")
            break


def validate_data(values):
    """
    Inside the Try, converts all the values to integers.
    Returns error if values can't be converted or if the values are less than 6.
    """
    try:
        [int(value) for value in values]
        if len(values) != 6:
            raise ValueError(
                f"Exactly 6 values required, you provided {len(values)}"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again. \n")
        return False
    
    return True


get_sales_data()