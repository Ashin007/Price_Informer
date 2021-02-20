import smtplib

import datetime

from bs4 import BeautifulSoup as bs
import urllib.request
page = urllib.request.urlopen("https://www.flipkart.com/dr-morepen-glucoone-bg-03-50-glucometer-strips/p/itm091d9067dcc0e?pid=GLTEFTX3TWGCHJWY&lid=LSTGLTEFTX3TWGCHJWYVDM9XO")
soup = bs(page, features="html.parser")
value = soup.find('div', class_="_30jeq3 _16Jk6d").string
price = int(value[1::])
print(price)



gmail_user = 'sample@gmail.om'
gmail_app_password = 'xxpasswordxx'

sent_from = gmail_user
sent_to = gmail_user
email_text = str(price)

date_and_time = str(datetime.datetime.now())


try:
    f = open("price_list.txt", "a")
    f.write("Price : "+str(price)+" Date: "+ date_and_time[:19]+"\n")
    f.close()

    if price > 700:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(gmail_user, gmail_app_password)
        server.sendmail(sent_from, sent_to, email_text)
        server.close()
        print('Email sent!')
except Exception as exception:
    print("Error: %s!\n\n" % exception)
