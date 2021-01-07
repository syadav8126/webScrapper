import spynner

browser = spynner.Browser()
url="https://www.moneycontrol.com/india/stockpricequote/banks-public-sector/statebankindia/SBI"

browser.load(url)
browser.runjs("get_FinancialTabData('income','S','S-income_statement','3');")

markup = browser._get_html()
