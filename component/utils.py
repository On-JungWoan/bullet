from os import path
from selenium import webdriver
from cases import build_obj

def pat_post_process(tree, idx:int,
        PAT:str, filter:str = '****PAT****'
    ) -> str:
    # try:
    return tree.xpath(PAT.replace(filter, f'{idx:02}'))[0]
    # except:
    #     return tree.xpath(PAT.replace(filter, idx))[0]

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