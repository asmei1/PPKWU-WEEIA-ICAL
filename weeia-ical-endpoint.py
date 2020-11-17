wfrom flask import Flask, request

app = Flask(__name__)


@app.route('/weeia_ical', methods=["GET"])
def string_api():
    month = request.args.get("month", None)
    year = request.args.get("year", None)

    return {"year": year, "month":month}



if __name__ == '__main__':
    app.run()
