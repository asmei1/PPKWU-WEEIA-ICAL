import datetime
from flask import Flask, request

app = Flask(__name__)


@app.route('/weeia_ical', methods=["GET"])
def string_api():
    dt = datetime.datetime.today()
    month = request.args.get("month", dt.month)
    year = request.args.get("year", dt.year)

    return {"year": year, "month":month}



if __name__ == '__main__':
    app.run()
