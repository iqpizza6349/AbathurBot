import requests
from bs4 import BeautifulSoup as bs

class LOL_Total():
    url = "https://www.op.gg/summoner/userName="
    headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WIn64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4130.116 Safari/537.36'
    }
    result = []
    def __init__(self, userName=None):
        self.userName = userName

    def set_userName(self, userName):
        self.userName = userName
    
    def run(self):
        res = requests.get(self.url + self.userName, headers=self.headers)
        self.parse_html(res.text)
        return res
    
    def parse_html(self, text):
        html = bs(text, 'html.parser')

        Tier = html.find('div', {'class': 'TierRank'})
        Tier = Tier.string if Tier else Tier
        Score = html.find('span', {'class' : 'LeaguePoints'})
        Score = Score.string if Score else Score
        Win = html.find('span', {'class' : 'wins'})
        Win = Win.string if Win else Win
        Lose = html.find('span', {'class' : 'losses'})
        Lose = Lose.string if Lose else Lose
        Odds = html.find('span', {'class' : 'winratio'})
        Odds = Odds.string if Odds else Odds
        
        sub_Tier = html.find('div', {'class': 'sub-tier__rank-tier'})
        sub_Tier = sub_Tier.string if sub_Tier else sub_Tier
        sub_WL = html.find('span', {'class': 'sub-tier__gray-text'})
        sub_WL = sub_WL.string if sub_WL else sub_WL
        sub_Odds = html.find('div', {'class': 'sub-tier__gray-text'})
        sub_Odds = sub_Odds.string if sub_Odds else sub_Odds
        #print(Tier, Score, Win, Lose, Odds)
        
        self.result.append({
            'Tier' : Tier,
            'Score' : Score,
            'Win' : Win,
            'Lose' : Lose,
            'Odds' : Odds,
            'sub_Tier' : sub_Tier,
            'sub_WL' : sub_WL,
            'sub_Odds' : sub_Odds
        })

    
    def get_result(self):
        if self.result:
            return self.result[-1]
        else:
            return None

if __name__ == "__main__":
      crawler = LOL_Total()
      while True:
            k = input("이름 >> ")
            crawler.set_userName(k)
            crawler.run()
            r = crawler.get_result()
            for v in r.values(): print(v)
            print("-"*50)