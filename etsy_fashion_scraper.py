import time
import requests
import os
import json
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class EtsyFashionScraper:

    def __init__(self):
        self.base_url = "https://etsy.com"
        self.driver = webdriver.Chrome()
        self.scraped_products = []

    def do_scraper_log(self, log_string=""):
        """
        Method for print formatted scraper log
        :param log_string: String to log on terminal
        :return:
        """
        print(f"[EstyFashionScraper]: {log_string}")

    def save_products(self):
        if len(self.scraped_products) > 0:
            file_name = "etsy_fashion_scraped_products.json"
            with open(file_name) as f:
                json.dump(self.scraped_products, f)
                self.do_scraper_log(f"Saved scraped product at: {file_name}")

    def go_to_clothes_category(self):
        pass

    def find_safe_value(self, content, tag, class_name=""):
        pass

    def parse_product_info(self, html_content_list):
        pass

    def grab_product_info(self):
        """
        Grab the products info e.g. product name, price and rating on current page
        :return:
        """
        pass

    def go_to_next_page(self):
        pass

    def download_product_images(self):
        """
        Method for downloading product images
        :return:
        """
        pass

    def scrape_fashion(self):
        pass


if __name__ == '__main__':
    etsyScraper = EtsyFashionScraper()
    etsyScraper.scrape_fashion()
