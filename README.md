# Requirements

## [selenium](https://pypi.python.org/pypi/selenium)

This package is used for interacting with the web content and scraping what is visible. To install:

`$ pip install -U selenium`

## [chromedriver](https://github.com/SeleniumHQ/selenium/wiki/ChromeDriver)

This is used for interfacing with the web content through selenium. You can usually point to your existing chrome browser if you have it installed on your system. Find out more by following the link.

## [pandas](http://pandas.pydata.org/)

This is used for post processing the scraped data. To install:

`$ conda install pandas` or `$ pip install pandas`

# Executing

After the requirements are fulfilled, run `scaper.py` using python:

`$ python scraper.py`

What you should obtain if it runs successfully are two files: `table.csv` and `random.csv` as included with this repository.