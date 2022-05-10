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
    print("Please enter sales data fromt the last market")
    print("Data should be six numbers, separated by commas")
    print("Example: 8,12,5,78,15,23")
    data_str = input("Enter your data here: ")
    print(f"User data: {data_str}")


get_sales_data()