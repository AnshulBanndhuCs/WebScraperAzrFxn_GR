import logging
import azure.functions as func
import sys
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
import undetected_chromedriver as uc
import config as Config

def main(req: func.HttpRequest) -> func.HttpResponse:


    logging.info('Python HTTP trigger function processed a request.')

    # Run the web scraping function
    logging.info('Running web scraper...')
 
    # initialize the driver and set the options
    options = uc.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-extensions")
    options.add_argument("headless")
    
    driver_path = Config.path
    driver = uc.Chrome(executable_path=driver_path, options=options)
    driver.get(Config.url)
    time.sleep(Config.scroll_sleep)
    driver.execute_script(Config.windScroll)
    time.sleep(Config.scroll_sleep)
    driver.execute_script(Config.windScroll)
    time.sleep(Config.scroll_sleep)
    driver.execute_script(Config.windScroll)
    time.sleep(Config.scroll_sleep)
    driver.execute_script(Config.windScroll)
    time.sleep(Config.scroll_sleep)
    driver.execute_script(Config.windScroll)
    time.sleep(Config.scroll_sleep)
    driver.execute_script(Config.windScroll)
    time.sleep(Config.scroll_sleep)
    xpath_list = [
        '//*[@id="inner-wrap"]/section/div/div[2]/header/h1',
        '//*[@id="post-27291"]/div/div[1]/h2[1]/strong',
        '//*[@id="post-27291"]/div/div[1]/h2[2]/strong',
        '//*[@id="post-27291"]/div/div[1]/h2[3]/strong',
        '//*[@id="post-27291"]/div/div[1]/h2[4]/strong',
        '//*[@id="post-27291"]/div/div[1]/h2[5]/strong'
    ]
    # list to store all the elements
    elements = []
    # loop through the XPATH expressions and find the corresponding element
    for xpath in xpath_list:
        element = driver.find_element(By.XPATH, xpath)
        elements.append(element)
    
    # loop through the elements and print their text values
    for element in elements:
        logging.info(element.text)
        print(element.text)
        # driver.quit()

    logging.info('Web scraping completed.')
    # print("Scraping completed.")
    
    # Return an HTTP response with status code 200
    return func.HttpResponse("Web scraping function executed successfully.", status_code=200)


main(func.HttpRequest)