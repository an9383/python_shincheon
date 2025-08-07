import pandas as pd
from bs4 import BeautifulSoup
import requests
from tqdm import tqdm


if __name__ == "__main__":
    tmp_data = []
    page = 1 # 1 ~ 49
    for i in range(1,50,1):
        url =f"https://www.hollys.co.kr/store/korea/korStore2.do?pageNo={i}"
        response = requests.get(url).text
        soup = BeautifulSoup(response, 'html.parser')
        table = soup.find('table')  # string
        trs = table.find_all('tr')  # 11 rows list
        leaves_table = [[td.text for idx, td in enumerate(tr.find_all('td')) if idx !=4] for jdx, tr in enumerate(trs) if jdx != 0]
        tmp_data += leaves_table
        holly_info_df = pd.DataFrame(tmp_data, columns=["지역","매장명","현황","주소","전화번호"])
        print(holly_info_df)
        holly_info_df.to_csv(('./data/holly_info.csv'),encoding='cp949')
