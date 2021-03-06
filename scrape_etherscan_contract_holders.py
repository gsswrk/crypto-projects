#!/usr/bin/python3

import re
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import sys

# pass contract address to pull all current token holders and output to file called "token_holders.txt"
contract_address = sys.argv[1]
driver = webdriver.Chrome()

driver.get(
    'https://etherscan.io/token/' + contract_address + '#balances')
WebDriverWait(driver, 10).until(
    EC.frame_to_be_available_and_switch_to_it((By.ID, "tokeholdersiframe")))
elements = WebDriverWait(driver, 20).until(EC.visibility_of_all_elements_located(
    (By.XPATH, '//*[@id="maintable"]/div[3]/table/tbody//tr/td[2]//a')))
text_file = open("token_holders.txt", "w")
for ele in elements:
    text = re.findall('[^=]*$', ele.get_attribute('href'))
    print(text[0])
    n = text_file.write(text[0]+'\n')
text_file.close()
