# API Documentation

This api will analyze WEEIA calendar (from [WEEIA](http://www.weeia.p.lodz.pl)) and returns a calendar
in ICAL format.
User could receive ICAL (.ics) file, compliant with the standard [RFC2455](https://www.ietf.org/rfc/rfc2445.txt) which contains WEEIA events. 

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

You can choose month and year from server should parse the calendar by use **month** and **year** params.
<br>
<br>
This example will get calendar for December 2020
```
    http://localhost:8080/weeia_ical?month=12&year=2020
```

Example of request for October 2020:
```
BEGIN:VCALENDAR
VERSION:2.0
PRODID:ics.py - http://git.io/lLljaA
BEGIN:VEVENT
DTSTART:20201008T000000Z
SUMMARY:Wielka Integracja WIP
UID:80e7c721-47ed-4364-bd35-f35e8efc2f08@80e7.org
END:VEVENT
BEGIN:VEVENT
DTSTART:20201010T000000Z
SUMMARY:Wielka Integracja WIP
UID:7496098a-e830-4d3e-b52b-2453f9fe3cbf@7496.org
END:VEVENT
BEGIN:VEVENT
DTSTART:20201009T000000Z
SUMMARY:Wielka Integracja WIP
UID:5b97f4b5-eb66-4036-973a-d14a95475c0d@5b97.org
END:VEVENT
END:VCALENDAR
```
If month param will be not given, actual will be taken.<br>
If year param will be not given, actual will be taken.

# Examples
Example .ics files could downloaded here:
<br>
<a href="march_weeia.ics" download="download"> March 2020 </a>
<br>
<a href="october_weeia.ics" download="download"> October 2020 </a>