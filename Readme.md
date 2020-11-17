# PPKWU_Task3_PPKWU_WEEIA_ICAL

## API Documentation

This api will analyze WEEIA calendar (from http://www.weeia.p.lodz.pl) and returns a calendar
in ICAL format.
User could receive ICAL which contains events WEEIA

## Run REST server
To run this FLASK server execute in console
```
  flask run
  ```

## API
To use server, send your GET request to endpoint:
```
    http://localhost:8080/weeia_ical
```


You can choose month and year from server should parse the calendar by use month and year params.
This example will get calendar for December 2020
```
    http://localhost:8080/weeia_ical?month=12&year=2020
```

If non params will be given, actual month will be taken.
