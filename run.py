import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('Portfolio 3 - Covid Stats')

def get_survey_data():

    """
    Get the most recent survey data from user
    """

    print ('Please enter survey data from the most recent respondent')
    print ('Data must be a string value and seperated by  commas')
    print ('Example: 1, Employed, 21 - 24, Female, Yes, Yes, Yes, No\n')

    data_str = input('Enter your data here: ')
    
    survey_data = data_str.split(",")
    validate_data(survey_data)

def validate_data(values):
    try:
        if len(values) != 8:
            raise ValueError(
                f"Exactly 8 values are required, you provided {len(values)}"
            )
    except ValueError as e: 
        print(f"Invalid data: {e}, please try again.")


get_survey_data()