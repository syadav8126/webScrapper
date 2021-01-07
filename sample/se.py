from selenium import webdriver
browser = webdriver.Firefox(executable_path="./geckodriver")
browser.get("https://www.python.org/")
print(browser.find_element_by_class_name("introduction").text)

browser.close()
