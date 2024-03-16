import requests
import json
from bs4 import BeautifulSoup

cookies = {
    'skid': '7696784131698244331',
    'yandexuid': '1907601651698244331',
    'yuidss': '1907601651698244331',
    'ymex': '2013604332.yrts.1698244332',
    '_ym_uid': '1698244331360239407',
    '_ym_d': '1698244331',
    'is_gdpr': '0',
    'is_gdpr_b': 'CLbVbBCJ1gE=',
    'yashr': '6547489991698244333',
    'yp': '1703383282.szm.1:1920x1080:958x951',
    'i': 'lyUW30rdCNoSt0eYRg3LD0IRyrFnF8jDgSTCzqgZW7pa3K3oI7Kf9mWbCqR4QoAr6UAx31QEOahlHN9+UdlGqx9wjPA=',
    'bltsr': '1',
    'receive-cookie-deprecation': '1',
    'bh': 'EkEiQ2hyb21pdW0iO3Y9IjEyMiIsICJOb3QoQTpCcmFuZCI7dj0iMjQiLCAiR29vZ2xlIENocm9tZSI7dj0iMTIyIhoFIng4NiIiDyIxMjIuMC42MjYxLjk1IioCPzAyAiIiOgkiV2luZG93cyJCCCIxMC4wLjAiSgQiNjQiUlsiQ2hyb21pdW0iO3Y9IjEyMi4wLjYyNjEuOTUiLCAiTm90KEE6QnJhbmQiO3Y9IjI0LjAuMC4wIiwgIkdvb2dsZSBDaHJvbWUiO3Y9IjEyMi4wLjYyNjEuOTUiWgI/MA==',
    '_ym_isad': '1',
    'gdpr': '0',
    '_ym_visorc': 'b',
    'KIykI': '1',
    'coockoos': '3',
    'bh': 'Ej8iQ2hyb21pdW0iO3Y9IjEyMiIsIk5vdChBOkJyYW5kIjt2PSIyNCIsIkdvb2dsZSBDaHJvbWUiO3Y9IjEyMiIaBSJ4ODYiIg8iMTIyLjAuNjI2MS45NSIqAj8wOgkiV2luZG93cyJCCCIxMC4wLjAiSgQiNjQiUloiQ2hyb21pdW0iO3Y9IjEyMi4wLjYyNjEuOTUiLCJOb3QoQTpCcmFuZCI7dj0iMjQuMC4wLjAiLCJHb29nbGUgQ2hyb21lIjt2PSIxMjIuMC42MjYxLjk1IiI=',
    'amcuid': '7056492761709467022',
    '_yasc': 'RBGYnsYdPAeNIWGHX1BSAztB9Arb5haT5MJSV/neUBSk0lKEyaeJivLp9u/yLrNIeTObkQ==',
}

headers = {
    'authority': 'yandex.ru',
    'accept': 'text/html, */*; q=0.01',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    # 'cookie': 'skid=7696784131698244331; yandexuid=1907601651698244331; yuidss=1907601651698244331; ymex=2013604332.yrts.1698244332; _ym_uid=1698244331360239407; _ym_d=1698244331; is_gdpr=0; is_gdpr_b=CLbVbBCJ1gE=; yashr=6547489991698244333; yp=1703383282.szm.1:1920x1080:958x951; i=lyUW30rdCNoSt0eYRg3LD0IRyrFnF8jDgSTCzqgZW7pa3K3oI7Kf9mWbCqR4QoAr6UAx31QEOahlHN9+UdlGqx9wjPA=; bltsr=1; receive-cookie-deprecation=1; bh=EkEiQ2hyb21pdW0iO3Y9IjEyMiIsICJOb3QoQTpCcmFuZCI7dj0iMjQiLCAiR29vZ2xlIENocm9tZSI7dj0iMTIyIhoFIng4NiIiDyIxMjIuMC42MjYxLjk1IioCPzAyAiIiOgkiV2luZG93cyJCCCIxMC4wLjAiSgQiNjQiUlsiQ2hyb21pdW0iO3Y9IjEyMi4wLjYyNjEuOTUiLCAiTm90KEE6QnJhbmQiO3Y9IjI0LjAuMC4wIiwgIkdvb2dsZSBDaHJvbWUiO3Y9IjEyMi4wLjYyNjEuOTUiWgI/MA==; _ym_isad=1; gdpr=0; _ym_visorc=b; KIykI=1; coockoos=3; bh=Ej8iQ2hyb21pdW0iO3Y9IjEyMiIsIk5vdChBOkJyYW5kIjt2PSIyNCIsIkdvb2dsZSBDaHJvbWUiO3Y9IjEyMiIaBSJ4ODYiIg8iMTIyLjAuNjI2MS45NSIqAj8wOgkiV2luZG93cyJCCCIxMC4wLjAiSgQiNjQiUloiQ2hyb21pdW0iO3Y9IjEyMi4wLjYyNjEuOTUiLCJOb3QoQTpCcmFuZCI7dj0iMjQuMC4wLjAiLCJHb29nbGUgQ2hyb21lIjt2PSIxMjIuMC42MjYxLjk1IiI=; amcuid=7056492761709467022; _yasc=RBGYnsYdPAeNIWGHX1BSAztB9Arb5haT5MJSV/neUBSk0lKEyaeJivLp9u/yLrNIeTObkQ==',
    'device-memory': '8',
    'downlink': '10',
    'dpr': '1',
    'ect': '4g',
    'referer': 'https://yandex.ru/pogoda/nizhny-novgorod?lat=56.326799&lon=44.00652',
    'rtt': '50',
    'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"',
    'sec-ch-ua-arch': '"x86"',
    'sec-ch-ua-bitness': '"64"',
    'sec-ch-ua-full-version': '"122.0.6261.95"',
    'sec-ch-ua-full-version-list': '"Chromium";v="122.0.6261.95", "Not(A:Brand";v="24.0.0.0", "Google Chrome";v="122.0.6261.95"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-model': '""',
    'sec-ch-ua-platform': '"Windows"',
    'sec-ch-ua-platform-version': '"10.0.0"',
    'sec-ch-ua-wow64': '?0',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
    'viewport-width': '1388',
    'x-requested-with': 'weather-front',
}

params = {
    'lat': '56.326799',
    'lon': '44.00652',
    'cameras': '0',
}

response = requests.get('https://yandex.ru/pogoda/segment/details', params=params, cookies=cookies, headers=headers).text

soup = BeautifulSoup(response,'lxml')


# with open(f'погода/1.html', 'w', encoding='utf-8') as file:  
#     json.dump(response, file, indent=4, ensure_ascii=False)

list_temp_weather = []
list_temp_day = []
x = []
temp_day = soup.find_all('div',class_='a11y-hidden')[::17]
for i in temp_day:
    list_temp_day.append(i.text)



temp_weather = soup.find_all(class_='weather-table__row')
for i_2 in temp_weather:
    weather = i_2.find(class_='a11y-hidden')
    list_temp_weather.append(weather.text)

weather_temp = list_temp_weather[1::4]


for day, weather in zip(list_temp_day, weather_temp):
    x.append({
        day:weather
    })
print(x)
with open(f'погода/1.json', 'w', encoding='utf-8') as file:  
    json.dump(x, file, indent=4, ensure_ascii=False) 

