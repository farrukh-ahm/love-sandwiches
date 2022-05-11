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
    return sales_data


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


def update_worksheet(data, worksheet):
    """
    Update the wroksheets.
    """
    print(f"Updating {worksheet} worksheet...")
    worksheet_to_update = SHEET.worksheet(worksheet)
    worksheet_to_update.append_row(data)
    print(f"Worksheet {worksheet} updated successfully!")


# def update_sales_worksheet(data):
#     """
#     Update sales worksheet, add new row with data provided.
#     """
#     print("Updating....")
#     sales_worksheet = SHEET.worksheet("sales")
#     sales_worksheet.append_row(data)
#     print("Update Successful!")


def calcualte_surplus_data(sales_row):
    """
    Calculate Surplus by comparing Sales with Stock
    """
    print("Calculating Surplus...")
    stock = SHEET.worksheet("stock").get_all_values()
    stock_row = stock[-1]
    surplus_data = []
    for stock, sales in zip(stock_row, sales_row):
        surplus = int(stock) - sales
        surplus_data.append(surplus)
    return surplus_data


def get_last_5_entries_sales():
    """
    Collects columns of data from sales worksheet. Returns the data as list of lists.
    """
    sales = SHEET.worksheet("sales")
    columns = []
    for i in range(1,7):
        column = sales.col_values(i)
        columns.append(column[-5:])
    return columns


def main():
    """
    Run all program functions
    """
    datas = get_sales_data()
    sales_data = [int(data) for data in datas]
    update_worksheet(sales_data, "sales")
    new_surplus_data = calcualte_surplus_data(sales_data)
    update_worksheet(new_surplus_data, "surplus")


print("Welcome to Love Sandwiches Data Automation:")
# main()
get_last_5_entries_sales()
sales_columns = get_last_5_entries_sales()