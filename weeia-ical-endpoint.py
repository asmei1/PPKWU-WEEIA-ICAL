import datetime
import requests
from ics import Calendar, Event
from flask import Flask, request
from bs4 import BeautifulSoup


app = Flask(__name__)
WEEIA_URL = "http://www.weeia.p.lodz.pl"


def parseWeeiaWebsite(year, month):
    URL = 'http://www.weeia.p.lodz.pl/pliki_strony_kontroler/kalendarz.php?rok=' + year + '&miesiac=' + month
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")

    result = soup.find(id="kalendarz")
    events = []
    for row in result.find_all("tr", {"class": "dzien"}):
        for day in row.find_all("a"):
            for inner_box in day.parent.find_all("div", {"class": "InnerBox"}):
                for e in inner_box.find_all("p"):
                    events.append(("".join(str(item) for item in e.contents),
                                   "".join(str(item) for item in day.contents)))

    return events


def prepareICal(year, month):
    cal = Calendar()
    for title, day in parseWeeiaWebsite(year, month):
        event = Event()
        event.name = title
        event.begin = year + "-" + month + "-" + day + "00:00:00"

        cal.events.add(event)
    return cal


@app.route('/weeia_ical', methods=["GET"])
def string_api():
    dt = datetime.datetime.today()
    month = request.args.get("month", dt.month)
    year = request.args.get("year", dt.year)


    return {"year": year, "month": month}



if __name__ == '__main__':
    app.run()
