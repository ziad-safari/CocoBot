from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



def BubbleTea(BubbleTea_products, BubbleTea_price):
    sold = []
    notsold = []

    for i in range(len(BubbleTea_products)):
        if BubbleTea_price[i].text[0] == "S":
            sold.append(BubbleTea_products[i].text)
        else:
            notsold.append(BubbleTea_products[i].text)
            
    return '\n'.join(map(str, sold))


        
