import time;
from selenium import webdriver;

Timer = 3 

Link = YOUR_YOUTUBE_LINK_HERE

views = NUMBER_OF_VIEWS_YOU_WANT_HERE

driver = webdriver.Chrome()
driver.get(Link)

for i in range(views):
    time.sleep(Timer)
    driver.refresh()
