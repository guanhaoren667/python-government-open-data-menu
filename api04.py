import requests
#115年竹風藝文饗宴節目表
#目標網址:https://odws.hccg.gov.tw/001/Upload/25/opendata/9059/300/2cc79cfc-0548-42c4-8703-988ac988d9c1.json?1150709152602
def api_04():
    url = "https://odws.hccg.gov.tw/001/Upload/25/opendata/9059/300/2cc79cfc-0548-42c4-8703-988ac988d9c1.json?1150709152602"
    resp = requests.get(url, verify=False, timeout=15)# 因資料來源的 SSL 憑證目前無法通過本機 Python 驗證，測試期間暫時關閉 HTTPS 憑證驗證。
    #print(resp)#確認回傳200
    data = resp.json()
    
    #print(type(data))
    #print(len(data))
    #print(data[0])
    
    for row in data:
        date = row['日期']
        showtime = row['時間']
        location = row['地點']
        content = row['活動節目']
        print("-----")
        print(f"日期: {date}")
        print(f"時間: {showtime}")
        print(f"地點: {location}")
        print(f"活動節目: {content}")