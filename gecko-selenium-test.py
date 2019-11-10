from time import sleep
from selenium import webdriver


def gecko_test(site_000='https://bit.ly/2WaKraO'):
    """
    simple overview:
        1) set up webdriver
        2) load this article 
        3) close up shop 
    
    input:
        >> site_000
            > default: url of this article
    """
    # set the driver 
    driver = webdriver.Firefox()

    # load this article 
    driver.get(site_000)
    # and chill a bit
    sleep(7)

    # k, cool. let's bounce. 
    driver.quit()


# make runable 
if __name__ == '__main__':
    # here we go
    gecko_test()