import requests



if __name__=="__main__":
    url = "https://www.coffeebeankorea.com/menu/list.asp?category=13"
    resp = requests.get(url)
    print(resp.text)

    with open('download.html', 'wb') as file:
        file.write(resp.content)