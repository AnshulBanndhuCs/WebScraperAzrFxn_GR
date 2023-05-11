from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
import undetected_chromedriver as uc
import pandas as pd


def scrapper():
    # initialize the driver and set the options
    options = uc.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-extensions")
    # options.add_argument("headless")
    
    driver_path = "E:\Office\PythonPrograms\WebScrapProject_01\Driver\chromedriver.exe"
    driver = uc.Chrome(executable_path=driver_path, options=options)
    driver.get("https://www.globotreks.com/destinations/india/fun-interesting-facts-india/")
    time.sleep(2)
    driver.execute_script("window.scrollBy(0, 500);")
    time.sleep(2)
    driver.execute_script("window.scrollBy(0, 500);")
    time.sleep(2)
    driver.execute_script("window.scrollBy(0, 500);")
    time.sleep(2)
    driver.execute_script("window.scrollBy(0, 500);")
    time.sleep(2)
    driver.execute_script("window.scrollBy(0, 500);")
    time.sleep(2)
    driver.execute_script("window.scrollBy(0, 500);")
    time.sleep(2)
    # element = driver.find_element(By.XPATH,'//*[@id="inner-wrap"]/section/div/div[2]/header/h1')
    # time.sleep(2)
    # element = driver.find_element(By.XPATH,'//*[@id="post-27291"]/div/div[1]/h2[1]/strong')
    # time.sleep(2)
    # element = driver.find_element(By.XPATH,'//*[@id="post-27291"]/div/div[1]/h2[2]/strong')
    # time.sleep(2)
    # element = driver.find_element(By.XPATH,'//*[@id="post-27291"]/div/div[1]/h2[3]/strong')
    # time.sleep(2)
    # element = driver.find_element(By.XPATH,'//*[@id="post-27291"]/div/div[1]/h2[4]/strong')
    # time.sleep(2)
    # element = driver.find_element(By.XPATH,'//*[@id="post-27291"]/div/div[1]/h2[5]/strong')
    # time.sleep(2)
    # list of XPATH expressions
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
        time.sleep(2)
    
    # loop through the elements and print their text values
    for element in elements:
        print(element.text)


#     # create a pandas DataFrame from the text list
# df = pd.DataFrame({"Data": text_list})

# # export the DataFrame to an Excel file
# df.to_excel("data.xlsx", index=False)
# driver.quit()

# scroll up the page by 1000 pixels
# driver.execute_script("window.scrollBy(0, -500);")
# wait for the page to load after scrolling
# time.sleep(2)
# scroll to the bottom of the page
# driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
# wait for the page to load after scrolling
# time.sleep(2)
# scroll to the top of the page
# driver.execute_script("window.scrollTo(0, 0);")
# wait for the page to load after scrolling
# time.sleep(2)

# find the element and get the text

# get the text of the element
# print the text to the console
# find all the search result links
# links = driver.find_elements_by_xpath("//h3[@class='r']/a")

# print the links
# for link in links:
#     print(link.get_attribute("href"))

# close the browser window

# In this example program, we first import the required modules - 
# webdriver and Keys from the selenium package, and time module for 
# waiting for the page to load.

# We then create an instance of the Chrome driver using the webdriver.Chrome() 
# function and set some options to maximize the browser window and 
# disable extensions. We also specify the path of the Chromedriver 
# executable file.

# Next, we navigate to the target website using the get() method of the 
# driver object and wait for the page to load using the time.sleep() function.

# We then find the search bar element on the page and enter a search
# query using the send_keys() method. We press the Enter key using the 
# Keys.RETURN constant.

# After waiting for the search results to load, we find all the 
# links to the search results using an XPath expression and print 
# them using the get_attribute() method.

# Finally, we close the browser window using the quit() method of the 
# driver object.