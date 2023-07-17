from os import path
from selenium import webdriver
from cases import build_obj

def pat_post_process(
        PAT:str, replace_value:str,
        filter:str = '****PAT****'
    ):
    return PAT.replace(filter, replace_value)


def load_chrome_driver(chrome_version):
    version = chrome_version.split('.')[0]
    driver_path = f'./driver/chromedriver_{version}.exe'
    
    if not path.isfile(driver_path):
        print('There is not matched chromedriver version.')
        # return webdriver.Chrome('chromedriver_113.exe')
        return webdriver.Chrome()
    # return webdriver.Chrome(driver_path)
    return webdriver.Chrome(driver_path)


def prepare(args):
    obj = build_obj(args)
    return obj