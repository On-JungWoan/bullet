from os import path
from cases import build_obj
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

def pat_post_process(tree, idx:int,
        PAT:str, filter:str = '****PAT****'
    ) -> str:
    # try:
    return tree.xpath(PAT.replace(filter, f'{idx:02}'))[0]
    # except:
    #     return tree.xpath(PAT.replace(filter, idx))[0]

def load_chrome_driver(chrome_version):
    version = chrome_version.split('.')[0]
    driver_path = rf'./component/driver/chromedriver_{version}.exe'
    
    if not path.isfile(driver_path):
        print('There is not matched chromedriver version.')
        # return webdriver.Chrome('chromedriver_113.exe')
        return webdriver.Chrome()
    service = Service(executable_path=driver_path)
    return webdriver.Chrome(service=service)

def prepare(args):
    obj = build_obj(args)
    return obj