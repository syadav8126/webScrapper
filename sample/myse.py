from selenium import webdriver
import time

browser = webdriver.Firefox(executable_path="./geckodriver")
browser.get("https://www.moneycontrol.com/india/stockpricequote/banks-public-sector/statebankindia/SBI")

elem = browser.find_elementis_by_name("li-S-income-3")

print(elem)
browser.close()
