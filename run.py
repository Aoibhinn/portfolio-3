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
    print ('Please enter survey data from the most recent respondent')
    print ('Data must be a string value and seperated by  commas')
    print ('Example: 1, Employed, 21 - 24, Female, Yes, Yes, Yes, No\n')

    data_str = input('Enter your data here: ')
    print(f"The data provided is {data_str}")


get_survey_data()