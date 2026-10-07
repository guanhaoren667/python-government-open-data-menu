import requests
#114學年度新竹市立國中小通訊資料
#目標網址:https://odws.hccg.gov.tw/001/Upload/25/opendata/9059/1910/5d949eea-d8f2-482a-8260-43c3f697dad2.json?1141121161504
def api_03():
    url = "https://odws.hccg.gov.tw/001/Upload/25/opendata/9059/1910/5d949eea-d8f2-482a-8260-43c3f697dad2.json?1141121161504"
    resp = requests.get(url, verify=False, timeout=15)# 因資料來源的 SSL 憑證目前無法通過本機 Python 驗證，測試期間暫時關閉 HTTPS 憑證驗證。
    #print(resp)#確認回傳200
    data = resp.json()
    
    #print(type(data))
    #print(len(data))
    #print(data[0])
    
    for row in data:
        name = row['學校']
        Tel = row['電話']
        address = row['地址']
        print("-----")
        print(f"學校: {name}")
        print(f"電話: {Tel}")
        print(f"地址: {address}")