import datetime
import requests
from ics import Calendar, Event
from flask import Flask, request, send_file
from bs4 import BeautifulSoup


app = Flask(__name__)

def parse_weeia_website(year, month):
    if len(month) <= 1:
        month = "0" + month

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


def prepare_ical(year, month):
    cal = Calendar()
    for title, day in parse_weeia_website(year, month):
        event = Event()
        event.name = title
        if int(day) < 10:
            day = "0" + day
        event.begin = year + "-" + month + "-" + day + "00:00:00"

        cal.events.add(event)
    return cal


@app.route('/weeia_ical', methods=["GET"])
def string_api():
    dt = datetime.datetime.today()
    year = request.args.get("year", str(dt.year))
    month = request.args.get("month", str(dt.month))

    cal = prepare_ical(year, month)

    import io
    f = io.BytesIO(str.encode(str(cal)))
    return send_file(f, mimetype="text/calendar")



if __name__ == '__main__':
    app.run()
