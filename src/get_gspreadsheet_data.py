# -*- coding: utf-8 -*-
import argparse
import gspread
from datetime import datetime
from oauth2client.service_account import ServiceAccountCredentials


def get_all_data():
    scope = ['https://spreadsheets.google.com/feeds']

    credentials = ServiceAccountCredentials.from_json_keyfile_name(
        'MozTWContributionLetter-e2d95d4347eb.json', scope)

    gc = gspread.authorize(credentials)

    # wks = gc.open("Where is the money Lebowski?").sheet1
    # wks = gc.open_by_url('https://docs.google.com/spreadsheets/d/1U41ouZnWU9Vnw-h9_4UQdxMy3f5jBhf48He1Sw6dxi4/edit#gid=1334835659')
    wks = gc.open_by_key('1U41ouZnWU9Vnw-h9_4UQdxMy3f5jBhf48He1Sw6dxi4').sheet1

    return wks.get_all_values()


def parse_time(time_str):
    return datetime.strptime(time_str, u'%Y-%m-%d-%H:%M:%S')

def filter_by_time(data, time_after):
    out = []
    for row in data:
        try:
            time = parse_time(row[0].encode('utf-8'))
            print(time)
            if time > time_after:
                out.append(row)
        except ValueError:
            # It's the header row
            continue
    return out


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument('after', action='store',
                        help='Only generate mails that are after this time. format: YYYY-mm-dd-HH:MM:SS')

    results = parser.parse_args()

    filter_by_time(get_all_data(), parse_time(results.after))

if __name__ == "__main__":
    main()
