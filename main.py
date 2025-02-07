##################### Extra Hard Starting Project ######################
import pandas
import datetime as dt
import random
import smtplib


# 1. Update the birthdays.csv
data = pandas.read_csv("birthdays.csv")
dict = data.to_dict(orient='records')
# for i in dict:
#     if i['email'] == 'test1234@email.com':
#         print(i)

# 2. Check if today matches a birthday in the birthdays.csv
now = dt.datetime.now()
yr = now.year
month = now.month
day = now.day
for i in dict:
    if i['year'] == yr and i['month'] == month and i['day'] == day:
        with open(f"letter_templates/letter_{random.randint(1, 3)}.txt") as letter:
            mail = letter.read()
            mail = mail.replace('[NAME]', i['name'])
            my_email = "lokispamzzzz@gmail.com"
            # "lokesh.chillmont@outlook.com"
            # "lokispamzzzz@gmail.com"
            passwd = "dnwmfvxpbhicuyjp"
            # outlook "lulvzprclgammssj"
            # "dnwmfvxpbhicuyjp" #google
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=my_email, password=passwd)
                connection.sendmail(
                    from_addr=my_email,
                    to_addrs="lokispamzzzz@gmail.com",
                    msg=f"Subject : Happy birthday\n\n {mail}"
                )

                # with open(f'letter_templates') as f:
                #     print(f)


# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv



# 4. Send the letter generated in step 3 to that person's email address.




