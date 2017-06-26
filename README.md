Contribution Letter Template
----------------------------------

# Fully automatic version
## Setting up
* Install Python 3 (I use 3.4)
* `pip install pytest` (You may consider using virtualenv: `virtualenv venv -p python3; source venv/bin/activate`)

## How it works
* The `src/mailer.py` is a AWS lambda code, it is responsible for generating the email content and send it through AWS SES service.
* The HTML form in `form/index.html` sends a POST request to the AWS API Gateway.
* The API Gateway triggers a the `src/mailer.py` lambda and generates the email.

## Testing
* To test the AWS lambda locally, run `python -m pytest tests`.
* All the unit/integration tests are in `tests/test_mailer.py`.

-----

# Google Spreadsheet + Offline version (deprecated)
## Setting up

http://gspread.readthedocs.io/en/latest/oauth2.html
* Go to Google Developer Console
* Create a project
* Enable the "Google Drive API" under the project
* Credentials Tab > New Credentials > Service Account Key
* App Engine blabla > JSON
* Download the JSON file
* Share the spreadsheet with the client email listed in the credential JSON file.

* `virtualenv _venv; source _venv/bin/activate`
* `pip install gspread oauth2client pytest`

## Usage

* Generate letters
```
cd src # You must be in the src folder to run compose.py
python compose.py <name> -i <interest areas>
```

e.g. 

```
python compose.py "Harry Potter" -i addons education qa
```

* Download the data from google form responses after a certain time

```
python get_gspreadsheet_data.py <YYYY-mm-dd-HH:MM:SS>
```

## Unit test
* `source _venv/bin/activate`
* `python -m pytest`

