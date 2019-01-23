#!/usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = "Francesco Loprete <f.loprete@protonmail.com>"
__date__ = "2019-01-23"
__version__ = "0.1"

import sys
from time import sleep
from selenium import webdriver
import unittest
from selenium.webdriver.support.select import Select

class TestSearchPage(unittest.TestCase):
    """
    The goal of this test is to verify the functionality of the searc page:
    https://www.autohero.com/de/search/

    The current functionality under test are:
    - Year filtering
    - View ordering (only price descending)

    """

    @classmethod
    def setUpClass(cls):
        "//a[ @class='btn btn-link' and contains(text(),'3')]"
        driver = webdriver.Firefox()
        driver.get("https://www.autohero.com/de/search/")
        element = driver.find_element_by_xpath("//span[text()='Erstzulassung ab']")
        element.click()
        select_year = Select(driver.find_element_by_name("yearRange.min"))
        select_year.select_by_value("5")
        select_sort = Select(driver.find_element_by_name("sort"))
        select_sort.select_by_value("2")
        cls.price_list = []
        cls.year_list = []
        # sleep is needed in order to prevent runtime errors
        sleep(1)
        while True:
            cars_table = driver.find_elements_by_xpath("//ul[@class='specList___2i0rY']")
            for car in cars_table:
                date = car.find_element_by_xpath("//li[@class='specItem___2gMHn']")
                cls.year_list.append(int(date.text.split('/')[1]))
                raw_price = car.find_element_by_xpath("//div[@data-qa-selector='price']")
                tmp = raw_price.text.split(' ')[0]
                cls.price_list.append(int(tmp.replace('.','')))
            if not cls.get_next_page(driver):
                break
        driver.close()

    @classmethod
    def tearDownClass(cls):
        del cls.price_list
        del cls.year_list

    @classmethod
    def get_next_page(cls, driver):
        current_page = int(driver.find_element_by_xpath("//li[ @class='active']//a").text)
        try:
            next_page = driver.find_element_by_xpath("//a[ @class='btn btn-link' and contains(text(),'{}')]".format(current_page+1))
        except:
            return None
        next_page.click()
        # sleep is needed in order to prevent runtime errors
        sleep(1)
        return True

    def test_descending_price_order(self):
        count_error_descending_price = 0
        previous = sys.maxint
        for price in self.price_list:
            if price > previous:
                count_error_descending_price += 1
            previous = price
        self.assertEqual(count_error_descending_price, 0)

    def test_car_first_registration_after_or_equal_2015(self):
        count_error_first_registration = 0
        for year in self.year_list:
            if year < 2015:
                count_error_first_registration += 1
        self.assertEqual(count_error_first_registration, 0)