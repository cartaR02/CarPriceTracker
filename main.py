from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import csv
import logging
from datetime import datetime
import requests
import gathering_sites
import car_html


logfile = "./logs/pull.{}.log".format(
    datetime.now().strftime("%Y %m %d_%H-%M")
)

logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s %(name)-12s %(levelname)-8s %(message)s",
        datefmt="%H:%M:%S",
        filename=logfile,
        filemode="w",
    )

console = logging.StreamHandler()
console.setLevel(logging.DEBUG)

formatter = logging.Formatter(
        "%(asctime)-12s: %(levelname)-8s %(message)s", datefmt="%H:%M.%S"
    )
console.setFormatter(formatter)

csv_file = "cars.csv"

with open(csv_file, "r") as urls:
    url_reader = csv.reader(urls)


    for row in url_reader:
        
        # sets the link to variable
        website_link = row[0]
        car_container = row[1]
        car_fields = row[2]

        # retrieves site from link
        website_link = car_html.car_string
        website_html = gathering_sites.get_website(website_link, True)
        
        all_containers = gathering_sites.find_all(website_html, car_container)

        title_identifier, price_identifier, color_indentifier = car_fields.split("|")
        for container in all_containers:
            try:
                title = container.find(title_identifier).text
                logging.info(title)
                price = container.find(class_ = price_identifier)
                logging.info(price.text)
                color = container.find(class_ = color_indentifier)
                logging.info(color)
            except Exception as err:
                logging.debug(container.prettify)
                logging.error(err)
                continue

        logging.info("***********************FINISHED")

