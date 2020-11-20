import requests
from bs4 import BeautifulSoup as bs

class lunch():
    url = "http://www.kyoha.ms.kr/wah/main/schoolmeal/calendar.htm?menuCode=103"
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WIn64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4130.116 Safari/537.36'
    }
    result = []

    def __init__(self, mark=None):
        self.mark = mark
    
    def set_mark(self, mark):
        self.mark
    
    def search(self):
        res = requests.get(self.url, headers=self.headers)
        self.parse_html(res.text)
        return res

    def parse_html(self, text):
        html = bs(text, 'html.parser')
        lunch = html.find('td', {'class': 'Contents_schoolmeal_ToDay'})
        sub_meal = lunch.find_all('div', {'class': 'Contents_schoolmeal_Txt'})
        meal = sub_meal[1]
        meal = meal.text
        menu = meal.split(')')
        length = len(menu)
        del menu[length-1]

        self.result.append({
            'menu' : menu
        })
        #for문으로 하나하나 인덱스를 꺼내서 출력한다.

    def get_result(self):
        if self.result:
            return self.result[-1]
        else:
            return None

'''
if __name__ == "__main__":
    crawler = lunch()
    k = input("mark >> ")
    crawler.set_mark(k)
    crawler.search()
    r = crawler.get_result()
    for v in r.values():
        print(v)
        print("*"*50)
    print("-"*50)
'''
