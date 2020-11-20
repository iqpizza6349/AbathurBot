#저 빈칸을 기점으로 하여 위에는 pip 혹은 기본적으로 주는 모듈이고, 아래에는 직접 만든 모듈이다.
import discord
import asyncio
from discord.ext import commands, tasks
from datetime import datetime

import random
import math
import time

import Nweather
import LOL
import Ndust
import Nfinedust
import duil_lunch
import kyoha_lunch

Token = ''
client = discord.Client()

@client.event
async def on_ready():
    print("EVOLUTION COMPLETE")
    await client.change_presence(activity=discord.Game("진화 연구"))

@client.event
async def on_message(message):
    author = message.author
    send = message.channel.send
    content = message.content

    if author == client.user:
        pass

    if content.startswith("%안녕"):
        embed = discord.Embed(
            description = "나는 아바투르. 진화구덩이의 연구자. 현재 자취 중. 왜 자취 중인지는 안 알려줌.",
            colour = 0x00FF00
        )
        await send(embed=embed)

    if content.startswith("%help"):
        embed = discord.Embed(
            title = "아바투르. 명령을 기다림.",
            description = "모든 명령어는 **`'%'`**를 필요로 함.",
            colour = 0x00FF00
        )
        embed.add_field(name="`안녕`", value="인사.", inline=False)
        embed.add_field(name="`너의 작업에 대해 말해봐`", value="나의 작업에 대해 설명함.", inline=False)
        embed.add_field(name="`(협동전 사령관들)`", value="예) `%짐레이너`", inline=False)
        embed.add_field(name="`갈치`", value="갈치인지 확인.", inline=False)
        embed.add_field(name="`ping`", value="너의 핑.", inline=False)
        embed.add_field(name="`날씨 (위치)`", value="예) `%날씨 서울 마포.`위치는 전국으로 제한됨.", inline=False)
        embed.add_field(name="`롤 전적 (이름)`", value="너의 롤 전적에 대해 설명.", inline=False)
        embed.add_field(name="`(사칙연산기호) (숫자1) (숫자2)`", value="예) `%+ 1 1`. `%- 3 2`. `%* 5 2`. `%/ 9 3`", inline=False)
        embed.add_field(name="`! (숫자)`", value="팩토리얼. 예) `%! 4`", inline=False)
        embed.add_field(name="`진화구덩이`", value="내가 있는 곳이 진화구덩이.", inline=False)
        embed.add_field(name="`진화`", value="변이하는 종 설명.", inline=False)
        embed.add_field(name="`변이`", value="변이하는 법을 설명.", inline=False)
        embed.add_field(name="`오늘`", value="시차 때문에 결과가 바뀔 수 도 있음.", inline=False)
        embed.add_field(name="`급식 (학교명)`", value="두일중과 교하중만 가능. [아직 불완전함. 하지만 가능.]", inline=False)
        embed.add_field(name="`버그제보`", value="벌레. 하지만 우리에게 해가 가는 벌레 제보 바람.", inline=False)

        await send(embed=embed)

    if content.startswith("%너의 작업에 대해 말해봐"):
        embed = discord.Embed(
            description="생명체를 볼 때,그 잠재력을 관찰, 유전자, 배열, 조작, 분리, 결합.\n\
                개선할 수 있는 방법을 찾음.\n\
                생명체를 먹고, 뼈를 으깸.\n\
                내 몸속에서 실험체를 만지고, 개조하고, 변경함.\n\
                훌룡하게 만듦.", 
            colour = 0x00FF00
        )

        embed1 = discord.Embed(
            description = "완벽하게가 아니고?",
            colour = 0x800080
        )

        embed2 = discord.Embed(
            description = "완벽은 없음.\n\
                완벽이라는 목표는 계속 변함.\n\
                멈추지 않음.\n\
                따라갈 수 있지만, 붙잡을 수 없음.\n\
                목적은 여왕이 결정함.\n\
                목적이 변하면, 군단도 변함.\n\
                이것이, 우리의 기능.",
            colour = 0x00FF00
        )

        await send(embed=embed)
        await asyncio.sleep(2)
        await send(embed=embed1)
        await asyncio.sleep(2)
        await send(embed=embed2)

    if content.startswith("%스투코프"):
        embed = discord.Embed(
            description = "생물체 스투코프.\n\
                대단히 흥미로움.\n\
                결과 충격적.\n\
                스투코프의 개조는 칼날 여왕의 개조에 버금감.\n\
                그러나 스투코프는 인위적인 설계의 산물.\n\
                테란과 저그 물질의 결합 솜씨.\n\
                흠이 없음.\n\
                극소 규모의 조작.\n\
                군단은 불가능.\n\
                투코프를 개조한 존재는 생물체 아바투르를 능가함.\n\
                반박할 수 없음.\n\
                군단을 데리고 즉시 그 존재의 밑으로 들어갈 것을 권함.",
            colour = 0x00FF00
        )

        embed1 = discord.Embed(
            title = "케리건",
            description = "절 대 안 돼.",
            colour = 0x800080
        )

        await send(embed=embed)
        await asyncio.sleep(4)
        await send(embed=embed1)

    if content.startswith("%갈치"):
        if author.id == 580699792712138762:
            await send("<@580699792712138762>")
            embed = discord.Embed(
                description = "테란. 미개하고 하등한 종족.",
                colour = 0x00FF00
            )
        else:
            embed = discord.Embed(
                description = "당신은 갈치가 아닙니다.",
                colour = 0x00FF00
            )
        await send(embed=embed)

    if content.startswith("%짐 레이너"):
        embed = discord.Embed(
            title = "감염된 해병", 
            description = "내가 너 때문에 저그가 되었어 이 개자식아",
            colour = 0xA0522D
        )
        embed1 = discord.Embed(
            title = "짐 레이너",
            description = "그게 내 잘못인가 친구?",
            colour = 0x2d5d83
        )
        await send(embed=embed)
        await asyncio.sleep(1.5)
        await send(embed=embed1)
        await asyncio.sleep(2)
        await send("`??? : 당신은 양심도 없습니까?`")
        await send("||아바투르 성우랑 감염된 해병 성우랑 같은 성우이다.||")

    if content.startswith("%케리건"):
        embed = discord.Embed(
            description = "넌 뭐지",
            colour = 0x800080
        )
        embed1 = discord.Embed(
            description = "아바투르. 군단 진화 및 유전자 조작. 처음엔 초월체, 이후 칼날 여왕을 섬겼음. 이제 당신을 섬김.",
            colour = 0x00FF00
        )
        embed2 = discord.Embed(
            description = "내가 칼날 여왕이다!",
            colour = 0x800080
        )
        embed3 = discord.Embed(
            description = "같지 않음. 유전 정보 조사. 칼날 여왕, 효율적. 고대 저그의 특성 보유. 테란의 영향 미미했음.\n\
                그 몸은, 테란 오염 심각함. 집게손 설계 형편없음. 개선 가능. 새로운 팔 달아 주겠음.",
            colour = 0x00FF00
        )
        embed4 = discord.Embed(
            description = "건드리기만 해 봐",
            colour = 0x800080
        )
        embed5 = discord.Embed(
            description = "목표는 군단의 진화. 모든 것에 완벽을 추구. 진화 구덩이에서 작업. 작업 상황, 이곳에서 확인 가능.",
            colour = 0x00FF00
        )
        await send(embed=embed)
        await asyncio.sleep(1)
        await send(embed=embed1)
        await asyncio.sleep(3)
        await send(embed=embed2)
        await asyncio.sleep(2)
        await send(embed=embed3)
        await asyncio.sleep(4)
        await send(embed=embed4)
        await asyncio.sleep(2)
        await send(embed=embed5)

    if content.startswith("%아르타니스"):
        embed = discord.Embed(
            title = "용기병(드라군)",
            description = "내가 돌아왔다. (난 분명 질럿이었던 것 같지만 기분 탓이겠지?)",
            colour = 0x4f9bd9
        )
        embed1 = discord.Embed(
            title = "아르타니스",
            description = "기분 탓이다 형제여",
            colour = 0x25c5df
        )
        await send(embed=embed)
        await asyncio.sleep(2)
        await send(embed=embed1)

    if content.startswith("%스완"):
        embed = discord.Embed(
            description = "로리 스완의 차량. 나약함. 비효율적. 저그의 울트라리스크가 더 효율적.",
            colour = 0x00FF00
        )
        embed1 = discord.Embed(
            description = "뭐가 어쩠다고 징그러운 괴물아?",
            colour = 0xe59400
        )
        await send(embed=embed)
        await asyncio.sleep(1.5)
        await send(embed=embed1)

    if content.startswith("%자가라"):
        embed = discord.Embed(
            description = "자가라가 만든 괴물, 아바투르는 도구에 불과함.",
            colour = 0x00FF00
        )
        await send(embed=embed)

    if content.startswith("%보라준"):
        embed = discord.Embed(
            description = "네라짐. 나약함. 아둔을 계속 믿음. 신앙심 깊은 종족",
            colour = 0x00FF00
        )
        embed1 = discord.Embed(
            title = "보라준",
            description = "아둔을 모욕하지 마라",
            colour = 0x540081
        )
        await send(embed=embed)
        await asyncio.sleep(1.5)
        await send(embed=embed1)

    if content.startswith("%노바"):
        embed = discord.Embed(
            description = "자치령 유령. 은폐 가능. 하지만 저그의 잠복보다는 비효율적임.",
            colour = 0x00FF00
        )
        embed1 = discord.Embed(
            title = "노바",
            description = "오늘은 저그를 사냥하는 날이군요.",
            colour = 0x008080
        )
        await send(embed=embed)
        await asyncio.sleep(2)
        await send(embed=embed1)

    if content.startswith("%아바투르"):
        msg = random.randrange(5)
        if (msg == 0):
            msg = "생물체 아바투르, 그 무엇보다 강함."
        elif (msg == 1):
            msg = "군단의 전략, 계산되고 효율적임. 적의 전략, 열등함."
        elif (msg == 2):
            msg = "진화는 계속됨, 군단은 더 강해짐."
        elif (msg == 3):
            msg = "유용한 전투였음, 많은걸 배움, 새로운 유전자를 만들어야 함."
        else:
            msg = "모든 경우에 대비할 수 있게 진화함. 적의 승리 가능성 없음."
        
        embed = discord.Embed(
            description = msg,
            colour = 0x00FF00
        )
        await send(embed=embed)

    if content.startswith("%카락스"):
        embed = discord.Embed(
            description = "케이다린 초석. 쓸모없음. 나약함. 비효율적. 방어적 용도로서 실패작임.",
            colour = 0x00FF00
        )
        embed1 = discord.Embed(
            title = "카락스",
            description = "케이다린 초석이 비싼 건 인정합니다. 하지만 나약하지는 않습니다.",
            colour = 0xffff00
        )
        await send(embed=embed)
        await asyncio.sleep(2)
        await send(embed=embed1)

    if content.startswith("%한과 호너"):
        embed = discord.Embed(
            description = "한과 호너. 호너는 한을 유전적으로 싫어함.",
            colour = 0x00FF00
        )
        embed1 = discord.Embed(
            title = "미라와 호너",
            description = "미라: `남편? 오늘은 함께, 저그를 상대하는거야.`  호너: (한숨) `좋아...`",
            colour = 0x702963
        )
        await send(embed=embed)
        await asyncio.sleep(2)
        await send(embed=embed1)
    
    if content.startswith("%알라라크"):
        embed = discord.Embed(
            description = "알라라크. 탈다림의 4번째 군주. 특징 : 츤데레임.",
            colour = 0x00FF00
        )
        embed1 = discord.Embed(
            title = "알라라크",
            description = "오, 저그가 이곳을 감염시켰다. 모조리 박멸해볼까.",
            colour = 0x400000
        )
        await send(embed=embed)
        await asyncio.sleep(2)
        await send(embed=embed1)

    if content.startswith("%타이커스"):
        embed = discord.Embed(
            description = "전설의 무법자. 하지만 자랑 아님.",
            colour = 0x00FF00
        )
        embed1 = discord.Embed(
            title = "타이커스",
            description = "이 저그 벌레들은 도무지 꺼져주지를 않는 다니까.",
            colour = 0x965a3e
        )
        await send(embed=embed)
        await asyncio.sleep(2)
        await send(embed=embed1)
    
    if content.startswith("%데하카"):
        embed = discord.Embed(
            description = "이 무리는 약하다. 무너질 거다.",
            colour = 0x00FF00
        )
        embed1 = discord.Embed(
            title = "데하카",
            description = "저그의 정수는 내가 수집한다.",
            colour = 0x72a0c1
        )
        await send(embed=embed)
        await asyncio.sleep(2)
        await send(embed=embed1)
    
    if content.startswith("%피닉스"):
        embed = discord.Embed(
            description = "피닉스. 저그에게 수없이 죽음. 이제는 약점 파악함.",
            colour = 0x00FF00
        )
        embed1 = discord.Embed(
            title = "피닉스",
            description = "이 저그를 해충처럼 박멸해주지.",
            colour = 0xffa500
        )
        await send(embed=embed)
        await asyncio.sleep(3)
        await send(embed=embed1)

    if content.startswith("%멩스크"):
        embed = discord.Embed(
            description = "아크튜러스 멩스크. 자치령의 전 황제. 지금은 칼날 여왕에게 최후를 맞이함.",
            colour = 0x00FF00
        )
        embed1 = discord.Embed(
            title = "멩스크",
            description = "군단은 그 자체로 문명에 대한 공격이다.",
            colour = 0xa52a2a
        )
        await send(embed=embed)
        await asyncio.sleep(4)
        await send(embed=embed1)

    if content.startswith("%제라툴"):
        embed = discord.Embed(
            description = "제일로 고생은 많이 함. 하지만 아르타니스한테 살해 당함.",
            colour = 0x00FF00
        )
        embed1 = discord.Embed(
            title = "제라툴",
            description = "적 저그가 목전에 있다.",
            colour = 0x008b8b
        )
        await send(embed=embed)
        await asyncio.sleep(3)
        await send(embed=embed1)

    if content.startswith("%스텟먼"):
        embed = discord.Embed(
            description = "나 다음으로 미친 놈. 기만자. 프로토스를 존경하는 것 같음.",
            colour = 0x00FF00
        )
        embed1 = discord.Embed(
            title = "스텟먼",
            description = "기계 군단, 저 녀석을 박살내 버려!",
            colour = 0xffa500
        )
        await send(embed=embed)
        await asyncio.sleep(2)
        await send(embed=embed1)

    if content.startswith("%ping"):
        embed = discord.Embed(
            description = "<@{0}>의 ping은 {1}ms임.".format(str(author.id), str(int(((round(client.latency, 3)))*10000))),
            colour = 0x00FF00
        )
        await send(embed=embed)

    if content.startswith("%날씨"):
        weather = Nweather.NaverWeather()
        dust = Ndust.NaverWeather()
        finedust = Nfinedust.NaverWeather()
        msg = content[4:]
        if (msg == ""):
            embed = discord.Embed(title="위치 설정 안됨.", description="`%날씨 위치`", colour=0x00FF00)
            pass
        else:
            weather.set_keyword(msg + "날씨")
            dust.set_keyword(msg + "미세먼지")
            finedust.set_keyword(msg + "초미세먼지")
            weather.run()
            dust.run()
            finedust.run()
            r = weather.get_result()
            r1 = dust.get_result()
            r2 = finedust.get_result()
            embed = discord.Embed(
                title = "현재 " + str(msg) + "의 날씨.",
                description = "날씨. 위치/시각/날씨 어제보다 비교/현재 온도 순서임.",
                colour = 0x00FF00
            )
            if (r['loc'] == None):
                embed.add_field(name="존재하지않는 위치이거나 외국입니다.", value="전국만 표시가능.", inline=False)
                pass
            else:
                embed.add_field(name="해당 위치.", value=r['loc'], inline=False)
                embed.add_field(name="시각.", value=r['time'], inline=False)
                embed.add_field(name="날씨.", value=r['status'], inline=False)
                embed.add_field(name="현재 온도.", value=r['degree'] + "℃", inline=False)
                embed.add_field(name="체감 온도.", value=r['sensible'] + "℃", inline=False)
                embed.add_field(name="현재 미세먼지.", value=str(r1['dust']) + "㎍/㎥", inline=False)
                embed.add_field(name="현재 초미세먼지.", value=str(r2['finedust']) + "㎍/㎥", inline=False)
        await send(embed=embed)

    if content.startswith("%롤 전적"):
        crawler = LOL.LOL_Total()
        msg = content[6:]
        crawler.set_userName(msg)
        crawler.run()
        r = crawler.get_result()

        embed = discord.Embed(
            title = "롤 정보.",
            description = str(msg) + "의 롤 전적.",
            colour = 0x00FF00
        )
        
        if (msg == ""):
            embed.add_field(name="이름 설정 안됨.", value="`%롤 전적 롤 닉`", inline=False)

        elif (r['Tier'] == None):
            embed.add_field(name = "존재하지않는 이름.", value="다시 한번 제대로 입력.", inline=False)

        elif r['Tier'].strip() == "Unranked" or r['Tier'] == "Unranked":
            embed.add_field(name="너의 티어", value=r['Tier'], inline=False)
            
            if r['sub_Tier'].strip() == "Unranked" or r['sub_Tier'] == "Unranked":
                embed.add_field(name="너는 언랭.", value="자유 랭도 없음.", inline=False)
            else:
                embed.add_field(name="너는 언랭.", value="하지만 자유랭은 있음.", inline=False)
                embed.add_field(name="너의 자유랭 티어.", value=r['sub_Tier'], inline=False)
                embed.add_field(name="너의 자유랭 점수(LP).", value="자유랭 점수는 크롤링 불가.", inline=False)
                embed.add_field(name="너의 자유랭 승패.", value=r['sub_WL'], inline=False)
                embed.add_field(name="너의 자유랭 승률.", value=r['sub_Odds'], inline=False)
        else:
            embed.add_field(name="너의 티어.", value=r['Tier'], inline=False)
            embed.add_field(name="너의 점수(LP).", value=r['Score'], inline=False)
            embed.add_field(name="너의 승리.", value=r['Win'], inline=False)
            embed.add_field(name="너의 패배.", value=r['Lose'], inline=False)
            embed.add_field(name="너의 승률.", value=r['Odds'], inline=False)

            if r['sub_Tier'].strip() == "Unranked" or r['sub_Tier'] == "Unranked":
                embed.add_field(name="너는 자유랭 없음.", value=None, inline=False)
            else:
                embed.add_field(name="너의 자유랭 티어.", value=r['sub_Tier'], inline=False)
                embed.add_field(name="너의 자유랭 점수(LP).", value="자유랭 점수는 크롤링 불가.", inline=False)
                embed.add_field(name="너의 자유랭 승패.", value=r['sub_WL'], inline=False)
                embed.add_field(name="너의 자유랭 승률.", value=r['sub_Odds'], inline=False)
        
        await send(embed=embed)

    if content.startswith("%+"):
        num = content[3:]
        num = num.split(" ")
        length = len(num)
        temp = 0
        for i in range(length):
            temp += int(num[i])
        await send("결과 : " + str(temp))
    
    if content.startswith("%-"):
        num = content[3:]
        num = num.split(" ")
        length = len(num)
        temp = int(num[0])
        for i in range(1, length):
            temp -= int(num[i])
        await send("결과 : " + str(temp))
    
    if content.startswith("%*"):
        num = content[3:]
        num = num.split(" ")
        length = len(num)
        temp = int(num[0])
        for i in range(1, length):
            temp *= int(num[i])
        await send("결과 : " + str(temp))

    if content.startswith("%/"):
        num = content[3:]
        num = num.split(" ")
        length = len(num)
        temp = int(num[0])
        okay = 0
        for i in range(1, length):
            try:
                temp /= int(num[i])
            except ZeroDivisionError:
                okay = 1
                pass
        if (okay == 0):
            await send("결과 : " + str(temp))
        else:
            await send("해당 값을 0으로 나눌 수 없습니다.")

    if content.startswith("%!"):
        num = int(content[3:])
        result = math.factorial(num)
        await send("팩토리얼 결과 : " + str(result))

    if content.startswith("%진화구덩이"):
        embed = discord.Embed(
            description = "훌륭하게 만듦.",
            colour = 0x00FF00
        )
        embed1 = discord.Embed(
            title = "케리건",
            description = "완벽하게가 아니고?",
            colour = 0x800080
        )
        embed2 = discord.Embed(
            description = "완벽은 없음. 완벽이라는 목표는 계속 변함. 멈추지 않음. 따라갈 수 있지만, 붙잡을 수 없음.",
            colour = 0x00FF00
        )
        await send(embed=embed)
        await asyncio.sleep(2)
        await send(embed=embed1)
        await asyncio.sleep(2)
        await send(embed=embed2)

    if content.startswith("%진화"):
        msg = content[4:]
        if (msg == ""):
            embed = discord.Embed(title = "진화시킬 유닛 선택 안 됨.", description = "`%진화 유닛`, 예) %진화 저글링", colour = 0x00FF00)

        elif (msg == "저글링"):
            embed = discord.Embed(title = "저글링. 변이 가능.", description = "`%변이 변종이름`", colour = 0x00FF00)
            embed.add_field(name="`랩터`", value="**날개 기능 향샹. 저글링 도약 가능.**", inline=False)
            embed.add_field(name="`군단충`", value="**부화기간 거의 없음. 고치 하나에 군단충 3마리 생성.**", inline=False)
        
        elif (msg == "맹독충"):
            embed = discord.Embed(title = "맹독충. 변이 가능.", description = "`%변이 변종이름`", colour = 0x00FF00)
            embed.add_field(name="`쌍독충`", value="**폭발 시 유체에서 새끼 맹독충 두 마리가 생성됨. 분열은 단 한 번만 발생.**", inline=False)
            embed.add_field(name="`사냥꾼`", value="**맹독충 도약 가능.**", inline=False)

        elif (msg == "바퀴"):
            embed = discord.Embed(title = "바퀴. 변이 가능.", description = "`%변이 변종이름`", colour = 0x00FF00)
            embed.add_field(name="`송장벌레`", value="**산성 타액은 살을 녹임. 숙주가 죽으면, 애바퀴가 나옴.**", inline=False)
            embed.add_field(name="`고름`", value="**바퀴 공격시 수축성 물질이 대상을 뒤덮어 막을 형성. 이동 속도 어려워짐. 공격 빈도 감소. 적을 약화시킴.**", inline=False)

        elif (msg == "히드라리스크"):
            embed = discord.Embed(title = "히드라리스크. 변이 가능.", description = "`%변이 변종이름`", colour = 0x00FF00)
            embed.add_field(name="`관통 촉수`", value="**단일 대상을 공격. 촉수로 쟝갑, 살갗, 뼈를 갈갈이 조각 냄.**", inline=False)
            embed.add_field(name="`가시 지옥`", value="**가시자옥은 잠복 상태에서 공격. 가시로 동시에 여러 적을 공격.**", inline=False)

        elif (msg == "군단 숙주"):
            embed = discord.Embed(title = "군단 숙주. 변이 가능.", description = "`%변이 변종이름`", colour = 0x00FF00)
            embed.add_field(name="`날벌레`", value="**날발레 둥지 유전자로 알주머니의 영구 변이 가능. 날아디는 식충 생성. 공격력 3 증가.**", inline=False)
            embed.add_field(name="`땅무지`", value="**먼지 벌레. 효소 분비물을 사용해 땅을 가르고 점막이 있는 곳으로 빠르게 이동.**", inline=False)

        elif (msg == "뮤탈리스크"):
            embed = discord.Embed(title = "뮤탈리스크. 변이 가능.", description = "`%변이 변종이름`", colour = 0x00FF00)
            embed.add_field(name="`무리군주`", value="**군단 종자. 대상에게 공생충 발사. 공생충은 지상 유닛을 공격하는 작은 생명체.**", inline=False)
            embed.add_field(name="`살모사`", value="**대상을 납치하고 마비 구름을 살포. 아군에 유리하도록 전장 교란.**", inline=False)

        elif (msg == "울트라리스크"):
            embed = discord.Embed(title = "울트라리스크. 변이 가능.", description = "`%변이 변종이름`", colour = 0x00FF00)
            embed.add_field(name="`녹시우스(독성)`", value="**자치령의 화합물. 흥미로움. 과학자들 군단을 진압하려다 우연히 강력한 독성 물질을 탄생시킴. 비저그 개체에 치명적. 독성 변종. 이 독성 물질과 영구히 결합하여, 유독 가스 형태로 방출. 독성 물질을 모아 갑피의 구멍으로 살포 가능.**", inline=False)
            embed.add_field(name="`토라스크`", value="**감염성 화합물과의 융합이 토라스크 변종 진화의 핵심. 이 과정에서 엄청난 에너지가 필요함. 과거엔, 초월체가 이 에너지 제공. 현재는 화합물이 조직을 흡수하면서 발생되는 에너지를 사용. 토라스크 변종. 죽으면 고치 상태로 돌입. 에너지를 사용해 조직 재생. 극도로 높은 회복력.**", inline=False)

        else:
            embed = discord.Embed(title = "변이시킬 유닛 선택 안 됨.", description = "`%진화 유닛`, 예) %진화 저글링", colour = 0x00FF00)

        await send(embed=embed)

    if content.startswith("%변이"):
        msg = content[4:]
        if (msg == ""):
            embed = discord.Embed(title = "해당 종 찾지 못함.", description = "`%변이 변종이름`, 예) %변이 랩터", colour = 0x00FF00)

        elif (msg == "랩터"):
            embed = discord.Embed(title = "저글링에서 랩터로 진화 완료.", description = "`부작용 : 없음.`", colour = 0x00FF00)

        elif (msg == "군단충"):
            embed = discord.Embed(title = "저글링에서 군단충로 진화 완료.", description = "`부작용 : 없음.`", colour = 0x00FF00)
        
        elif (msg == "쌍독충"):
            embed = discord.Embed(title = "맹독충에서 쌍독충로 진화 완료.", description = "`부작용 : 없음.`", colour = 0x00FF00)
        
        elif (msg == "사냥꾼"):
            embed = discord.Embed(title = "맹독충에서 사냥꾼로 진화 완료.", description = "`부작용 : 없음.`", colour = 0x00FF00)
        
        elif (msg == "송장벌레"):
            embed = discord.Embed(title = "바퀴에서 송장벌레로 진화 완료.", description = "`부작용 : 없음.`", colour = 0x00FF00)
        
        elif (msg == "고름"):
            embed = discord.Embed(title = "바퀴에서 고름로 진화 완료.", description = "`부작용 : 체력 25 감소.`", colour = 0x00FF00)
        
        elif (msg == "관통 촉수"):
            embed = discord.Embed(title = "히드라리스크에서 관통 촉수로 진화 완료.", description = "`부작용 : 단일공격. 공중 공격 불가.`", colour = 0x00FF00)
        
        elif (msg == "가시 지옥"):
            embed = discord.Embed(title = "히드라리스크에서 가시 지옥로 진화 완료.", description = "`부작용 : 공중 공격 불가.`", colour = 0x00FF00)

        elif (msg == "무리 군주"):
            embed = discord.Embed(title = "뮤탈리스크에서 무리 군주로 진화 완료.", description = "`부작용 : 공중 공격 불가.`", colour = 0x00FF00)

        elif (msg == "살모사"):
            embed = discord.Embed(title = "뮤탈리스크에서 살모사로 진화 완료.", description = "`부작용 : 직접적 공격 불가.`", colour = 0x00FF00)

        elif (msg == "날벌레"):
            embed = discord.Embed(title = "군단 숙주의 식충을 날벌레로 진화 완료.", description = "`부작용 : 식충 체력 15 감소.`", colour = 0x00FF00)
        
        elif (msg == "땅무지"):
            embed = discord.Embed(title = "군단 숙주에서 땅무지로 진화 완료.", description = "`부작용 : 점막이 있는 곳에서만 이동 가능.`", colour = 0x00FF00)

        elif (msg == "녹시우스(독성)"):
            embed = discord.Embed(title = "울트라리스크에서 녹시우스(독성)으로 진화 완료.", description = "`부작용 : 없음.`", colour = 0x00FF00)
        
        elif (msg == "토라스크"):
            embed = discord.Embed(title = "울트라리시크에서 토라스크로 진화 완료.", description = "`부작용 : 없음.`", colour = 0x00FF00)

        else:
            embed = discord.Embed(title = "해당 종 찾지 못함.", description = "`%변이 변종이름`, 예) %변이 랩터", colour = 0x00FF00)
    
        await send(embed=embed)

    if content.startswith("%오늘"):
        year = time.strftime("**%Y**", time.localtime(time.time()))
        month = time.strftime("**%m**", time.localtime(time.time()))
        date = time.strftime("**%d**", time.localtime(time.time()))
        day = time.strftime("%A", time.localtime(time.time()))
        #day는 요일이다.

        if (day == "Monday"):
            day = "**월요일**"
        elif (day == "Tuesday"):
            day = "**화요일**"
        elif (day == "Wednesday"):
            day = "**수요일**"
        elif (day == "Thursday"):
            day = "**목요일**"
        elif (day == "Friday"):
            day = "**금요일**"
        elif (day == "Saturday"):
            day = "**토요일**"
        elif (day == "Sunday"):
            day = "**일요일**"
        else:
            day = "**Bad ERROR :(**"

        embed = discord.Embed(
            title = "**오늘의 날짜.**",
            description = "오늘에 대해서 설명.",
            colour = 0x00FF00
        )
        embed.add_field(name="연도", value=str(year), inline=False)
        embed.add_field(name="월", value=str(month), inline=False)
        embed.add_field(name="일", value=str(date), inline=False)
        embed.add_field(name="요일", value=str(day), inline=False)

        await send(embed=embed)

    if content.startswith("%급식"):
        msg = content[4:]

        if (msg == ""):
            embed = discord.Embed(
                title = "학교 지정되지않았음.",
                description = "%급식 학교",
                colour = 0x00FF00
            )
        elif (msg == "두일중" or msg == "두일중학교"):
            crawler = duil_lunch.lunch()
            crawler.search()
            r = crawler.get_result()
            embed = discord.Embed(
                title = "두일중학교 급식.",
                description = "괜찮을... 안 괜찮을 지는 모름.",
                colour = 0x00FF00
            )
            for i in range(len(r['menu'])):
                embed.add_field(name="** **", value=r['menu'][i] + ")", inline=False)
        
        elif (msg == "교하중" or msg == "교하중학교"):
            crawler = kyoha_lunch.lunch()
            crawler.search()
            r = crawler.get_result()
            embed = discord.Embed(
                title = "교하중학교 급식.",
                description = "괜찮을... 안 괜찮을 지는 모름.",
                colour = 0x00FF00
            )
            for i in range(len(r['menu'])):
                embed.add_field(name="** **", value=r['menu'][i] + ")", inline=False)

        else:
            embed = discord.Embed(
                title = "해당 학교 발견하지 못함.",
                description = "급식 명령어는 두일중학교와 교하중학교만 출력가능함.",
                colour = 0x00FF00
            )
        await send(embed=embed)
    
    if content.startswith("%버그제보"):
        embed = discord.Embed(
            title="버그발생. 개발자한테 dm혹은 이메일 보내길 권고. 빠른 시일 내에 개발자가 수정할 것임.",
            description="개발자 디코 : IQPIZZA6349#8983, 이메일 : iqpizza62@gmail.com",
            colour = 0x00FF00
        )
        await send(embed=embed)

    #2020.11.16 기준 718ln, 80KB

client.run(Token)
