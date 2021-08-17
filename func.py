import requests
import datetime

from keys import api

# 今日の色々を取得する関数
def request(url):
    newData = {}
    response = requests.get(url)
    data = response.json()["current"]
    ok = ["pressure","humidity","temp"]
    for i in ok:
        newData[i] = data[i]
    newData["weather_id"] = data["weather"][0]["id"]
    newData["weather_icon"] = data["weather"][0]["icon"]
    newData["moon"] = moon_age()
    now = datetime.datetime.now()
    newData["year"] = now.year
    newData["month"] = now.month
    newData["day"] = now.day
    newData["time"] = time()
    return newData

# 月齢を調べる関数
def moon_age():
    now = datetime.date.today()
    Y, M, D = now.strftime("%Y/%m/%d").split("/")
    y = int(Y)
    m = int(M)
    d = int(D)
    mp = [0,2,0,2,2,4,5,6,7,8,9,10]
    return (((y - 11) % 19) * 11 + mp[m - 1] + d) % 30

def time():
    day = datetime.date.today()
    now = datetime.datetime.now().time()
    times = [
        datetime.time(8,40,0),
        datetime.time(9,40,0),
        datetime.time(10,40,0),
        datetime.time(11,40,0),
        datetime.time(13,35,0),
        datetime.time(14,35,0),
        ]
    dif = []

    for i in times:
        td = abs(datetime.datetime.combine(day, i) - datetime.datetime.combine(day, now))
        dif.append(td)
    
    return dif.index(min(dif))


if __name__ == "__main__":
    print(request("https://api.openweathermap.org/data/2.5/onecall?lon=140.47670066333643&lat=37.759109816261606&units=metric&lang=ja&appid={}".format(api())))