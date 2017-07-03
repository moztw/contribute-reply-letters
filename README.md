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

# Setting up the AWS server
* Create an AWS account
* Switch the region to US West (Oregon), or other region that supports SES (email) service.
## Lmabda
* Services => AWS Lambda
* Create a Lambda function
* Select the "hello-world-python3" template
* Select the "API Gateway" as the trigger
  * API name: "ReplyEmail"
  * Security: "Open"
* In the Configure function page
  * Name: ReplyEmail
  * Description: Send an email based on contributor's interest
  * Runtime: Python 3.6
  * Copy the generated code into the "Lambda function code" section
  * Role: Create a custom role => A new IAM management page will pop up
    * IAM Role: create a new IAM Role
    * Role Name: lmabda_email
    * Show Policy Document => Edit => Paste the following:
```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "logs:CreateLogGroup",
        "logs:CreateLogStream",
        "logs:PutLogEvents"
      ],
      "Resource": "arn:aws:logs:*:*:*"
    },
{
       "Effect": "Allow",
       "Action": ["ses:SendEmail", "ses:SendRawEmail"],
       "Resource":"*"
     }
  ]
}
```

## API Gateway
* Services => API Gateway
* Select `/ReplyEmail`, click "Actions" => Create Method => Select POST
* In the POST setting
  * Integration type: Lambda function
  * Lambda Region: us-west-2 (Oregon)
  * Lambda Function: "ReplyEmail"
* Select `/ReplyEmail` => Actions => Enable CORS
* Select `/ReplyEmail` => Actions => Deploy API
* (optional) Delete the auto-generated "ANY" method by selecting it => Actions => Delete Method

* You'll see an "Invoke URL", you can now test it with:

```
curl \
  -H "Content-Type: application/json" \
  -X POST \
  -d '{"name":"foo","email":"shing.lyu@gmail.com"}' \
  https://XXXXXXXX.execute-api.us-west-2.amazonaws.com/prod/ReplyEmail
```




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

