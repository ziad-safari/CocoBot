import discord 
from selenium import webdriver
from CheckDrinks import BubbleTea
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

chrome = r"C:\Users\Ziad\Downloads\chromedriver_win32\chromedriver.exe" #my chrome path
driver = webdriver.Chrome(chrome)

#Lester Coco Website
driver.get("https://gosnappy.io/owa/snappy/detail/G2991/3012/m/menu_60") 

driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
time.sleep(5)


milktea_products = driver.find_elements(By.CLASS_NAME, "px-2.pt-2.text-xs-left.font-weight-bold.menu-title.menu-title-mobile")
milktea_price = driver.find_elements(By.CLASS_NAME, "price.font-weight-bold")

client = discord.Client()

@client.event
async def on_ready():
    print(
        'We have logged in as {0.user}'.format(client)
    )

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!milktea'):
        await message.channel.send('SOLD OUT: \n' + BubbleTea(milktea_products, milktea_price))


client.run('OTIxNjE5OTU1Njg0ODg0NDkx.Yb1jeA.x8jpCjwCFep8BIr6p_ZiqqCcEu0')