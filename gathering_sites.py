from bs4 import BeautifulSoup
import bs4
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

######### selenium settings ########## hell yeah jigsaw you the goat
options = Options()
# makes it so browser doesn't open when webdriver is activated
options.headless = True 
# set our webdriver to firefox with the options we specified
driver = webdriver.Firefox(options=options)

def find_all(current_html: bs4.BeautifulSoup,
                    link_identifier: str) -> list:
    # TODO Make more generic
    container_list = current_html.find_all(class_ = link_identifier)

    return container_list


def get_website(website_link: str, Testing: bool) -> bs4.BeautifulSoup:

    if not Testing:
        driver.get(website_link)

        web_request_info = driver.page_source
    else:
        web_request_info = website_link
    webpage_html: bs4.BeautifulSoup = BeautifulSoup(
            web_request_info, "html.parser"
        )
    driver.quit()
    return webpage_html
