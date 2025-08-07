import requests




if __name__ == "__main__":
    url = "https://finance.naver.com/"
    resp = requests.get(url).text
    print(resp)