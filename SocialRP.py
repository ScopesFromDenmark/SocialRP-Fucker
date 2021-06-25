from selenium import webdriver
from time import sleep
import os
import random
driver = webdriver.Chrome()
driver.get('https://socialrp.dk/register')
os.system('cls')
print('SOCIALRP Fucker')
print('SOCIALRP Fucker')
print('SOCIALRP Fucker')
print('SOCIALRP Fucker')
print('SOCIALRP Fucker')
print('SOCIALRP Fucker')
print('SOCIALRP Fucker')
print('SOCIALRP Fucker')
print('Vent 5 Sekunder')
sleep(5)
driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div[2]/form/div[1]/div/a').send_keys('dinfar#0001')
driver.find_element_by_xpath('//*[@id="name"]').send_keys( random.choice('a b c d e f g h i j k l m n o p q r s t u v w x y z') + 'FuckingTabere' ) #BrugerNavn
sleep(1)
driver.find_element_by_xpath('//*[@id="surname"]').send_keys( random.choice('a b c d e f g h i j k l m n o p q r s t u v w x y z') )  #IRL NAvn
driver.find_element_by_xpath('//*[@id="birthday"]').clear()
driver.find_element_by_xpath('//*[@id="birthday"]').send_keys('16-11-1996')  #Fødsels Dato
driver.find_element_by_xpath('//*[@id="email"]').send_keys( random.choice('a b c d e f g h i j k l m n o p q r s t u v w x y z') + '@gmail.com' )  #email
driver.find_element_by_xpath('//*[@id="password"]').send_keys('LorteSikkerHed123') #Password
driver.find_element_by_xpath('//*[@id="password-confirm"]').send_keys('LorteSikkerHed123') #Bekræft Password
driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div[2]/form/div[8]/div/button').click()






