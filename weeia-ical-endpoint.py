import datetime
import requests
from flask import Flask, request
from bs4 import BeautifulSoup


app = Flask(__name__)
WEEIA_URL = "http://www.weeia.p.lodz.pl"


def parseWeeiaWebsite(month, year):
    page = requests.get(WEEIA_URL)
    soup = BeautifulSoup(page.content, "html.parser")

    result = soup.find(id="kalendarz")
    days = []
    for row in result.find_all("tr", {"class": "dzien"}):
        for day in row.find_all("a"):
            print(day.contents)



parseWeeiaWebsite(0, 0)


@app.route('/weeia_ical', methods=["GET"])
def string_api():
    dt = datetime.datetime.today()
    month = request.args.get("month", dt.month)
    year = request.args.get("year", dt.year)


    return {"year": year, "month": month}



if __name__ == '__main__':
    app.run()
