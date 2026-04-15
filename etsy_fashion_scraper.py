import time
import requests
import os
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class EtsyFashionScraper:

    def __init__(self):
        self.base_url = "https://etsy.com"

    def do_scraper_log(self, log_string=""):
        """
        Method for print formatted scraper log
        :param log_string: String to log on terminal
        :return:
        """
        pass

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

