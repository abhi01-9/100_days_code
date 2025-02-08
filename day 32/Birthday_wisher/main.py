import smtplib
import datetime as dt
import random

MY_EMAIL = "email@gmail.com"
MY_PASSWORD = "password"
now = dt.datetime.now()
weekday = now.weekday()

if weekday == 0:
    with open("quotes.txt") as quote_file:
        all_quote = quote_file.readlines()
        quote = random.choice(all_quote)
    print(quote)
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="abhibhaskar76342@gmail.com",
            msg=f"Subject:Monday Motivation\n\n {quote}")

# import smtplib
#
# my_email = "email@gmail.com"
# password = "password"
#
# with smtplib.SMTP("smtp.gmail.com",587) as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs="abhibhaskar76342@gmail.com",
#         msg="Subject:Hello\n\n This is the body of my email")

# import datetime as dt
#
# now = dt.datetime.now()
# year = now.year
# day_of_week = now.weekday()
# print(day_of_week)
#
# date_of_birth = dt.datetime(year=1998, month=2, day=5)
#
# print(date_of_birth)
