import pandas
import datetime as dt
import random
import smtplib


# read
data = pandas.read_csv("birthdays.csv")
dict_ = data.to_dict(orient='records')
# for i in dict:
#     if i['email'] == 'test1234@email.com':
#         print(i)

# if today the birthdays.csv
now = dt.datetime.now()
yr = now.year
month = now.month
day = now.day
for i in dict_:
    if i['year'] == yr and i['month'] == month and i['day'] == day:
        with open(f"letter_templates/letter_{random.randint(1, 3)}.txt") as letter:
            mail = letter.read()
            mail = mail.replace('[NAME]', i['name'])
            my_email = "your_emailid"  
            passwd = "your_passwd"
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=my_email, password=passwd)
                connection.sendmail(
                    from_addr=my_email,
                    to_addrs="your_emailid",
                    msg=f"Subject : Happy birthday\n\n {mail}"
                )

                



