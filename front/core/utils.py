from telnetlib import EC
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.expected_conditions import element_to_be_clickable
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import WebDriverException, TimeoutException
#import pandas as pd
from datetime import date, datetime
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import os
from core.models import *


def get_files_directory():
    dir_path = r'/descargas'

    # list to store files
    res = []
    # Iterate directory
    for file_path in os.listdir(dir_path):
        # check if current file_path is a file
        if os.path.isfile(os.path.join(dir_path, file_path)):
            # add filename to list
            res.append(file_path)
    return res
