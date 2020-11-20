import requests
from bs4 import BeautifulSoup as bs

class NaverWeather():
      url = "https://search.naver.com/search.naver?sm=top_hty&fbm=1&ie=utf8&query="
      headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WIn64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4130.116 Safari/537.36'
      }
      result= []

      def __init__(self, keyword=None):
            self.keyword = keyword

      def set_keyword(self, keyword):
            self.keyword = keyword

      def run(self):
            res = requests.get(self.url + self.keyword, headers=self.headers)
            self.parse_html(res.text)
            return res

      def parse_html(self, text):
            html = bs(text, 'html.parser')

            finedust = html.find('em', {'class': 'main_figure'})
            finedust = finedust.string if finedust else finedust

            self.result.append({
                  'finedust' : finedust
            })

      def get_result(self):
            if self.result:
                  return self.result[-1]
            else:
                  return None
'''
if __name__ == "__main__":
      crawler = NaverWeather()
      while True:
            k = input("지역 이름 >> ")
            crawler.set_keyword(k + "초미세먼지")
            crawler.run()
            r = crawler.get_result()
            for v in r.values(): print(v)
            print("-"*50)
'''