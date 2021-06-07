import os
import selenium
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from datetime import date,timedelta
import mysql.connector
import json

today = date.today() - timedelta(days=1)

# dd/mm/YY
d1 = today.strftime("%d/%m/%Y")
options = Options()
options.headless = True
driver = webdriver.Chrome(ChromeDriverManager().install())
settingsOpen = open("settings.json", "r")
settingsRead = settingsOpen.read()
settingsJSON = json.loads(settingsRead)
url = "https://instagram.com/" + settingsJSON['username'] + "/"
driver.get(url)
driver.implicitly_wait(10)
driver.find_element_by_xpath('/html/body/div[2]/div/div/button[1]').click()

posts = driver.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/ul/li[1]/a').text
followers = driver.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/ul/li[2]/a').text
following = driver.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/ul/li[3]/a').text
name = driver.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/div[2]/h1').text
username = driver.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/div[1]/h2').text
bio = driver.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/div[2]/span').text

imgsrc = driver.find_element_by_xpath('//html/body/div[1]/section/main/div/header/div/div/div/button/img[contains(@class, "be6sR")]')
pimg = imgsrc.get_attribute("src")

mydb = mysql.connector.connect(
  host = settingsJSON['sql']['servername'],
  user = settingsJSON['sql']['user'],
  password = settingsJSON['sql']['pass'],
  database = settingsJSON['sql']['database']
)

mycursor = mydb.cursor()

sql = "INSERT INTO " + settingsJSON['sql']['table'] + " (date, followers, following, posts, name, bio, username, pimg) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
val = (d1, followers, following, posts, name, bio, username, pimg)
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")
driver.close()
quit()
