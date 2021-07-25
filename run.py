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
    while True:

        print('Please enter the most recent number of confirmed covid cases')
        print('This data must be for Ireland, Germany, France, Italy, Cyprus, and Sweden')
        print('Example: 201, 0, 13, 54, 66, 87\n')

        data_str = input('Enter your data here: ')

        survey_data = data_str.split(",")

        if validate_data(survey_data):
            print('Data is valid!')
            break

    return survey_data


def validate_data(values):
    try:
        if len(values) != 6:
            raise ValueError(
                f"Exactly 6 values are required, you provided {len(values)}"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.")
        return False
    return True


def update_survey_worksheet(data):
    print('Updating survey worksheet...\n')
    survey_worksheet = SHEET.worksheet('survey')
    survey_worksheet.append_row(data)
    print("survey worksheet successfully updated.\n")


def update_recovered_worksheet(data):
    print('Updating recovered worksheet...\n')
    recovered_worksheet = SHEET.worksheet('recovered')
    recovered_worksheet.append_row(data)
    print("Recovered worksheet successfully updated.\n")


def calculate_recovered_data(survey_row):
    print('Calculating recovered cases...\n ')
    death = SHEET.worksheet('confirmed_deaths').get_all_values()
    death_row = death[-1]

    recovered_data = []
    for death, survey in zip(death_row, survey_row):
        recovered = survey - int(death)
        recovered_data.append(recovered)

    return recovered_data


def main():
    data = get_survey_data()
    survey_data = [int(num) for num in data]
    update_survey_worksheet(survey_data)
    new_recovered_data = calculate_recovered_data(survey_data)
    update_recovered_worksheet(new_recovered_data)


main()
