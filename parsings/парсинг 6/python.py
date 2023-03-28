import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver


def get_data(url):
    headers = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "accept-language": "ru,en;q=0.9,en-GB;q=0.8,en-US;q=0.7",
        "cache-control": "max-age=0",
        "connection": "keep-alive",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.51"
    }

    r = requests.get(url=url, headers=headers)

    with open("index.html", "w", encoding="utf-8") as file:
        file.write(r.text)

    # get hotels urls
    r = requests.get("https://api.rsrv.me/hc.php?a=hc&most_id=1317&l=ru&sort=most", headers=headers)
    soup = BeautifulSoup(r.text, "lxml")

    hotels_cards = soup.find_all("div", class_="hotel_card_dv")

    for hotel_url in hotels_cards:
        hotel_url = hotel_url.find("a").get("href")
        print(hotel_url)




def main():
    get_data("https://www.tury.ru/hotel/most_luxe.php")
    # get_data_with_selenium("https://www.tury.ru/hotel/most_luxe.php")


if __name__ == '__main__':
    main()