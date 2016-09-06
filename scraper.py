# Author: Bharat Kunwar
# 22 May 2016
# http://github.com/brtknr/SeleniumScraper

import os
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException

# Provide full location of your chrome driver
chromedriver = "/Users/bharatkunwar/Desktop/chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver)
# Enter the webpage you want to get
url = "https://www.cortalconsors.fr/euroWebFr/-?$part=financeinfosHome.Desks.funds.Desks.snapshot.Desks.quotes.Desks.historicalquotes.content.timesandsales.body.historicalquotes&$event=page&id=LU0326422689&id_name=ISIN&offset=0"
driver.get(url)
select = Select(driver.find_element_by_name('range'))
# Select option on a drop down menu
select.select_by_value('36m')
# Find button by name so that we can click it
button=driver.find_element_by_name('$$event_historical')
button.click()
page = 1
table = {}

# Load data from page
while True:
	try:
		table[page] = driver.find_element_by_class_name('table-ew').text
		page += 1
		a=driver.find_element_by_class_name('nav')	
		a.find_element_by_link_text(str(page)).click()
	except StaleElementReferenceException:		
		pass
	except NoSuchElementException:
		break;

# We are now done with Selenium
driver.quit()

# Post processing in Pandas
import pandas
df = pandas.DataFrame(columns=['Opening','High','Low','Fenced','Volume'])
"""Post processing to csv"""
for i in range(len(table)):
	for row in table[i+1].split('\n')[2:-1]:
		f = row.split(' ')
		df.loc[f[0]] = f[1:]

df.index = pandas.to_datetime(df.index,dayfirst=True)
df.sort_index()
df.to_csv('table.csv')

# Sample of the whole dataset
import random
s=random.sample(range(750),100)
randoms = df.iloc[s].sort_index()
randoms.to_csv('randoms.csv')