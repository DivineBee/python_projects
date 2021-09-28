import requests
from datetime import datetime as dt
import smtplib
import time

MY_LAT = 47.033135
MY_LONG = 28.786908


def near_iss():
    response_iss = requests.get(url="http://api.open-notify.org/iss-now.json")
    response_iss.raise_for_status()

    latitude = float(response_iss.json()["iss_position"]["latitude"])
    longitude = float(response_iss.json()["iss_position"]["longitude"])

    if MY_LAT-5 <= latitude <= MY_LAT+5 and MY_LONG-5 <= longitude <= MY_LONG+5:
        return True


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }
    response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()

    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = dt.now()

    if sunrise >= time_now.hour >= sunset:
        return True


while True:
    time.sleep(60)
    if is_night() and near_iss():
        my_email = "my_email"
        password = "password"

        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email,
                                to_addrs=my_email,
                                msg=f"Look up, ISS is approaching")