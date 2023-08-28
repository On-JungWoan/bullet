import re
from os import path
from cases import build_obj
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

def pat_post_process(tree, idx:int, filter:str = '****PAT****', **pat_dict
    ) -> str:
    res = []

    for key, val in pat_dict.items():
        try:
            tmp = tree.xpath(val.replace(filter, f'{idx:02}'))[0]
        except:
            tmp = tree.xpath(val.replace(filter, f'{idx}'))[0]
        
        if key == 'DATE_PAT':
            res.append(
                ''.join(re.findall('[^a-zA-Z긱-힣]', tmp.strip())).strip()
            )
        else:
            res.append(tmp.strip())

    return res

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