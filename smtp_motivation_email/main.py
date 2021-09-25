import smtplib
import datetime as dt
import random

now = dt.datetime.now()
day_of_week = now.weekday()
if day_of_week == 0:
    quotes = []
    with open("quotes.txt") as file:
        quotes = [n for n in file]
    quote = random.choice(quotes)

    my_email = "my_email"
    passwordd = "passwordd"

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=passwordd)
        connection.sendmail(from_addr=my_email,
                            to_addrs=my_email,
                            msg=f"Subject:Motivation\n\n{quote}")


