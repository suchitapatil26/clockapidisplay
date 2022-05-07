# clockapidisplay
Humanreadable format display using REST api

The Django framework is used to build the REST api for humanreadable clock.

the inflect package is used for converting the number into word format.

to run the code command used : python manage.py runserver

the time paramenter (hh:mm) passed as a string through URL.

the code running on localhost

e.g of URL: http://127.0.0.1:8000/clockapi/time/16:45/

the last parameter in URL is time which displayed in the human readable output in the JSON format.
