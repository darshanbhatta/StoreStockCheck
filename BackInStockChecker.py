#this program is used to send a text message to a user when an item is available. The code and be customized and can work on any site, this one works on bestbuy.com

from twilio.rest import Client

from time import sleep

from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import TimeoutException


#create and config the browser
options = webdriver.ChromeOptions()
options.add_argument('headless')
browser = webdriver.Chrome(chrome_options=options)

#change this to your item/website you want to be notified by
browser.get("https://www.bestbuy.com/site/toshiba-43-class-led-2160p-smart-4k-uhd-tv-with-hdr-fire-tv-edition/6194907.p?skuId=6194907")

# the following line needs your Twilio Account SID and Auth Token
client = Client("ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx", "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")

booolean = True 

while booolean:
    try:

        #change this element finder to match your website
        text=browser.find_element_by_id("pdp-add-to-cart-button").text
        
        #change the compared String to match your website
        if str(text) != "Add to Cart":

            #refreshes the browser if the item is not in stock
            browser.refresh()
            print(text + " first")

        else:

            print(text + " second")

            #sends a text to the user when the item is in stock
            client.messages.create(to="+1xxxxxxxxxx", from_="+1xxxxxxxxxx", body="Item is back on sale!")

            browser.quit()

            booolean = False
      
    except:
        print(text + " fail")
    
    #adds a ten second delay each time it refreshes the browser
    sleep(10)
