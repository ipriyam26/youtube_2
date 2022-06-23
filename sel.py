
import contextlib
import os
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from random import randint
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.firefox.options import Options as FirefoxOptions
import glob
import geckodriver_autoinstaller


import ssl

# This restores the same behavior as before.


# TODO Rename this here and in `upload`
def submitted(uploaded_videos, path, gave_error):
    uploaded_videos.append(path)
    print_status(len(uploaded_videos), len(gave_error))
    time.sleep(800)

def print_status( total_uploaded,  total_errors):
    os.system("clear")
    print(f"Total Uploaded = {total_uploaded}")
    print(f"Total Error = {total_errors}")



def upload(wait):
    geckodriver_autoinstaller.install()
    profile = webdriver.FirefoxProfile(
        '/Users/ipriyam26/Library/Application Support/Firefox/Profiles/8yd0fdlp.tthots')
    profile.set_preference("dom.webdriver.enabled", False)
    profile.set_preference('useAutomationExtension', False)
    profile.update_preferences()
    options = FirefoxOptions()
    options.headless = True
    desired = DesiredCapabilities.FIREFOX
    driver = webdriver.Firefox(firefox_profile=profile,
                            desired_capabilities=desired, 
                            options=options)
    gave_error = []
    i=0
    uploaded_videos=[]
    for path in glob.glob('videos/*.mp4'):
        if(path in uploaded_videos):
            continue
        try:
            driver.get("https://www.youtube.com/upload")
            driver.fullscreen_window()
            driver.implicitly_wait(5)
            elem = driver.find_element_by_xpath("//input[@type='file']")
            try:
                elem.send_keys(f"/Users/ipriyam26/Programing/TT/{path}")
                r = randint(75,125)/10.0
                # time.sleep(600)
                time.sleep(r)
                next_button = driver.find_element_by_xpath('//*[@id="next-button"]')
                next_button.click()
                r= randint(30,55)/10.0
                time.sleep(r)
                next_button.click()
                r= randint(30,55)/10.0
                time.sleep(r)
                next_button.click()
                # next_button = driver.find_element_by_xpath('//*[@id="next-button"]')
                #submit
                time.sleep(3.3)
                driver.find_element_by_xpath('//*[@id="done-button"]').click()
                r = randint(30,55)/10.0
                time.sleep(r)
                submitted(uploaded_videos, path, gave_error)
            except Exception:
                gave_error.append(path)
            while gave_error:
                for video in gave_error:
                    driver.get("https://www.youtube.com/upload")
                    driver.implicitly_wait(5)
                    elem = driver.find_element_by_xpath("//input[@type='file']")
                    with contextlib.suppress(Exception):
                        elem.send_keys(f"/Users/ipriyam26/Programing/TT/{video}")
                        r = randint(65,105)/10.0
                        time.sleep(r)
                        box = driver.find_element_by_xpath('//*[@id="scrollable-content"]')
                        r = randint(45,75)/10.0
                        time.sleep(r)
                        box.send_keys(Keys.END)
                        r = randint(65,75)/10.0
                        time.sleep(r)
                        next_button = driver.find_element_by_xpath('//*[@id="next-button"]')
                        next_button.click()
                        r= randint(30,55)/10.0
                        time.sleep(r)
                        next_button.click()
                        r= randint(30,55)/10.0
                        time.sleep(r)
                        next_button.click()
                        time.sleep(r)
                        driver.find_element_by_xpath('//*[@id="done-button"]').click()
                        r = randint(30,55)/10.0
                        time.sleep(r)
                        gave_error.remove(video)
                        submitted(uploaded_videos, path, gave_error)
        except Exception:
            time.sleep(wait)

    driver.close()
    # os.system("reddit")


if __name__ == "__main__":
    # This restores the same behavior as before.
    context = ssl._create_unverified_context()
    upload()