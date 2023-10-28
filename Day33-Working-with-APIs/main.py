import requests
from datetime import datetime
import smtplib

MY_EMAIL = "varunthapa615@gmail.com"
MY_PASSWORD = "mesfsdmjqqxxtyny"

MY_LATITUDE = 29.3595500
MY_LONGITUDE = 79.5549060


def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")

    response.raise_for_status()

    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if MY_LATITUDE - 5 <= iss_latitude <= MY_LATITUDE + 5 and MY_LONGITUDE - 5 <= iss_longitude <= MY_LONGITUDE + 5:
        return True


def is_night():
    parameter = {

        "lat": 29.3595500,
        "lng": 79.5549060,
        "formatted": 0

    }
    response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameter)
    response.raise_for_status()
    data = response.json()

    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour

    if time_now >= sunset or time_now <= sunrise:
        return True


if is_night() and is_iss_overhead():
    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(MY_EMAIL, MY_PASSWORD)
    connection.sendmail(
        from_addr=MY_EMAIL,
        to_addrs=MY_EMAIL,
        msg="Subject:Look UP☝️!\n\nThis will see the ISS over there..."
    )






