from bs4 import BeautifulSoup
import lxml
import requests
import smtplib
import schedule

my_email = ""
password = ""

PRODUCT_URL = input("Enter url of desired product: ")
desired_price = float(input("Insert the desired product price: "))
to_address = input("Write your email: ")
# PRODUCT_URL = "https://www.amazon.com/SilverStone-Technology-Strider-Platinum-PS-ST85F-PT/dp/B01GPNHNAA/ref=sr_1_4?keywords=psu+80+plus&qid=1638890162&s=amazon-devices&sr=1-4"
header_params = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36 OPR/81.0.4196.60",
    "Accept-Language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7"
}
response = requests.get(PRODUCT_URL, headers=header_params)

webpage = response.text
soup = BeautifulSoup(webpage, "lxml")

title = soup.find(id="productTitle").get_text().strip()

price_raw = soup.find(name="span", class_="a-price a-text-price a-size-medium apexPriceToPay")
price = float(price_raw.getText().split("$")[1])
print(price)


def send_email():
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(my_email, password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=to_address,
                            msg=f"Subject:Amazon Best Price\n\nThe price for:\n{title}\n has dropped. Now it is {price}")


while True:
    schedule.run_pending()
    if price <= desired_price:
        schedule.every().day.at("10:30").do(send_email)
