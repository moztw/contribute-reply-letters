Contribution Letter Template
----------------------------------

# Setting up

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

# Usage

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

# Unit test
* `source _venv/bin/activate`
* `python -m pytest`

