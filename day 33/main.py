from http.client import responses
from datetime import datetime
import smtplib
import requests
from numpy.ma.core import masked_greater
import time

MY_EMAIL = "email@gmail.com"
MY_PASSWORD = "password"

# if our request succeeded it give response code 200
"""
1xx: Hold On
2XX: Here you go
3XX: Go Away
4XX: You screwed up
5XX: I screwed up
"""

MY_LAT = 51.507351
MY_LONG = -0.127758


def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    iss_longitude = float(data["iss_position"]["longitude"])
    iss_latitude = float(data["iss_position"]["latitude"])

    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_latitude <= MY_LAT + 5:
        return True


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()

    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour

    if time_now >= sunset or time_now <= sunrise:
        return True

while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs="receiver@gmail.com",
                msg=f"Subject:Look\n\n The ISS is above the sky "
            )

