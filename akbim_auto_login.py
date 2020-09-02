from selenium import webdriver
import time

username = input("TC : ")
password = input("Şifre : ")

browser = webdriver.Firefox()

url = "http://obs.finalokullari.com.tr/"

browser.get(url)
time.sleep(2)

usr_username = browser.find_element_by_xpath('//*[@id="username"]')
usr_password = browser.find_element_by_xpath('//*[@id="password"]')
usr_giris    = browser.find_element_by_xpath('/html/body/div[2]/div[1]/section/div/div/div[2]/div/div[2]/div/div[1]/div[2]/form/div[4]/button')


usr_username.send_keys(username)
usr_password.send_keys(password)

usr_giris.click()

