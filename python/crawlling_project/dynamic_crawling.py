from selenium.webdriver.common.alert import Alert
from setting import chrome_driver
import time
from selenium.webdriver.common.by import By
import requests
from bs4 import BeautifulSoup
from tqdm import tqdm
import pandas as pd

def get_table(driver):
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    table = soup.find('table')  # string
    trs = table.find_all('tr')  # 11 rows list
    leaves_table = [[td.text for idx, td in enumerate(tr.find_all('td')) if idx != 4] for jdx, tr in enumerate(trs) if
                    jdx != 0]
    return leaves_table

if __name__ == "__main__":
    tmp_data = []
    # url="https://category.gmarket.co.kr/listview/L100000002.aspx"
    # resp = requests.get(url).text
    # html = BeautifulSoup(resp,'html.parser')
    # datum = html.select_one("#cppLargeCategoryBest > li:nth-child(1) > div.name > a").text
    # print(datum)

    url = "https://www.hollys.co.kr/store/korea/korStore2.do"
    driver = chrome_driver()
    driver.get(url)

    # exit()
    # driver.find_element(By.XPATH, '''//*[@id="contents"]/div[2]/fieldset/fieldset/div[2]/a[7]''').click()
    tmp_data = []
    for page in tqdm(range(2,11)):
        if page%10 == 1:
            if page == 11:
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(1)
                driver.find_element(By.XPATH,'''//*[@id="contents"]/div[2]/fieldset/fieldset/div[2]/a[10]/img''').click()
                time.sleep(1)
                leaves = get_table(driver)
            else:
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(1)
                driver.find_element(By.XPATH,'''//*[@id="contents"]/div[2]/fieldset/fieldset/div[2]/a[11]/img''').click()
                time.sleep(1)
                leaves = get_table(driver)
        else:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(1)
            driver.find_element(By.LINK_TEXT, f'{page}').click()
            time.sleep(1)
            leaves = get_table(driver)
        tmp_data += leaves
        dynamic_df = pd.DataFrame(tmp_data, columns=["지역","매장명","현황","주소","전화번호"])
        print(dynamic_df)
        # dynamic_df.to_csv(('./data/dynamic_info.csv'),encoding='cp949')
        dynamic_df.to_csv(('./data/dynamic_info.csv'), encoding='utf-8')

    # main_window = driver.current_window_handle
    # for handle in driver.window_handles:
    #     if handle != main_window:
    #         driver.switch_to.window(handle)
    #         driver.close()
    #         print("팝업 창이 자동으로 닫혔습니다.")
    #         break
    # driver.switch_to.window(main_window)
    # time.sleep(2)
    # driver.find_element(By.XPATH,'''/html/body/div[2]/div[1]/div[1]/ul[3]/li[1]/a/img''').click()
    # time.sleep(50)







